from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO,emit
import time
import openai
import openpyxl 
import re
import tiktoken
import apikey
import time
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
socketio = SocketIO(app,cors_allowed_origins="http://localhost:5173")
@app.route('/')
def hello_world():
    return 'Connected to server'
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files["file"]
    filename = file.filename
    print(filename)
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 
    file.save('upload/' + file.filename)
    def num_tokens_from_string(string: str, encoding_name: str) -> int:
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens
    system_prompt = """bạn là một phiên dịch viên tiếng nhật sang tiếng việt trong lĩnh vực IT. 
    hãy dịch những nội dung bên dưới sang tiếng việt theo phong cách dùng trong IT.
    nội dung cần dịch một câu sẽ theo định dạng bên dưới, tôi sẽ gửi nhiều câu trong một tin nhắn: 
    {{code}}:{{câu cần dịch}}

    trong đó câu cần dịch có thể nhiều dòng. dấu xuống dòng là @NEW_LINE_MARK@ và hãy giữ nguyên.

    Format tin nhắn của user sẽ như trong cặp dấu () sau:
    (
    INPUT
    ------
    A1: 更新履歴
    D6: 案件を選択

    GH25:-問い合わせる案件を選択してください。
    AH25:-画面ID

        作成者

    D7: 案件を選択

    )

    Format trả lời sẽ như bên dưới trong cặp dấu ():
    (
    RESULT
    ------
    A1: Lịch sử
    D6: Lựa chọn Anken
    GH25:-Hãy lựa chọn Anken contact
    AH25:-ID màn hình

        Người tạo

    D7: Lựa chọn Anken
    )
    hãy dịch toàn bộ tin nhắn  sang tiếng việt với cùng định dạng như trên, nếu bạn không thể dịch được thì hãy để trống nội dung phía sau dấu. Nếu nội dung cần dịch chứa tiếng việt hoặc tiếng anh thì cụm tiếng việt/ tiếng anh đó không cần dịch."""

    def translate(sheet):
        token = 0
        token_accumulator = 0
        openai.api_key = apikey.api_key
        for row in sheet.iter_rows():
            row_str = ""
            for cell in row:
                if cell.value is not None and isinstance(cell.value, str) and not cell.value.isascii():
                    row_str += """
                        {}:{}""".format(cell.coordinate, cell.value.replace("\n", " @NEW_LINE_MARK@ "))
            if row_str != "":
                messages=[
                        {
                            "role": "system", "content": system_prompt,
                        },
                        {
                            "role": "user", "content": """
                                INPUT
                                ------
                                {}
                            """.format(row_str),
                        },
                    ]
                token_accumulator += (num_tokens_from_string((' '.join(str(e) for e in messages)), "cl100k_base"))
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages = messages
                    )
                except Exception as e:
                    print("Rate limit exceeded. Please try again later.")
                    print(e)
                    continue
                print(token_accumulator)
                if (token_accumulator > 20000):
                    print("30s until next request")
                    time.sleep(30)
                    print("continue")
                    token_accumulator = 0
                token += response['usage']['total_tokens']
                translated = response['choices'][0]['message']['content']

                regex = r"([a-z]+\d+):(.+)"
                matches = re.finditer(regex, translated, re.MULTILINE | re.IGNORECASE)
                for matchNum, match in enumerate(matches, start=1):
                    sheet[match.group(1)].value = match.group(2).replace(" @NEW_LINE_MARK@ ", "\n")
                    # print(f"set {match.group(1)}={match.group(2)}")
        return token
    def duplicate_worksheets(input, output):
        total_tokens = 0
        workbook = openpyxl.load_workbook(input)
        sheet_names = workbook.sheetnames
        for sheet_name in sheet_names:
            original_sheet = workbook[sheet_name]
            total_tokens += translate(original_sheet)
            workbook.save(output)
        return total_tokens
    input = './upload/' + file.filename
    output = './output.xlsx'
    total_tokens = duplicate_worksheets(input, output)
    print("Total tokens: {}".format(total_tokens))
    return jsonify({'message': 'File translated successfully'})
if __name__ == '__main__':
    socketio.run(app)

