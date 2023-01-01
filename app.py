from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

mybot = ChatBot(
    "Chatterbot",
    preprocessors=["chatterbot.preprocessors.clean_whitespace"],
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    statement_comparison_funtion = "LevenshteinDistance",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi, mình không hiểu. Bạn thử hỏi lại xem.',
            'self.select_response': 'chatterbot.response_selecttion.get_first_response', 
            'maximum_similarity_threshold': 0.9
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi, mình không hiểu. Bạn thử hỏi lại xem.',
            'self.select_response': 'chatterbot.response_selecttion.get_first_response', 
            'maximum_similarity_threshold': 0.6
        }
    ]
    )
mybot.storage.drop()
trainer = ChatterBotCorpusTrainer(mybot)
trainer.train("chatterbot.corpus.Vi-vn")

@app.route("/")
def home():             
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(mybot.get_response(userText).confidence)
    return str(mybot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)