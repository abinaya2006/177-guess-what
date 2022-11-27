from flask import Flask,render_template,jsonify,request
import random


app=Flask(__name__)

templates=[
    {
        "story_id":"1",
        "inputs":4,
        "category": "I have teeth but can’t eat. What am I?",
        "word": "Comb"
    },
    {
        "story_id":"2",
        "inputs": 4,
        "category": "What kind of tree can you carry in your hand",
        "word": "Palm"
    },

    {
        "story_id":"3",
        "inputs": 4,
        "category": "What can one catch that is not thrown?",
        "word": "Cold"
    },
    
    {
        "story_id":"4",
        "inputs": 6,
        "category": "The first modern Olympic Games were held in which country?",
        "word": "Greece"
    },
    
    {
        "story_id":"5",
        "inputs": 8,
        "category": "What starts with “e” and ends with “e” but only has one letter in it?",
        "word": "Envelope"
    },

    {
        "story_id":"6",
        "inputs": 12,
        "category": "What can you hold without touching it at all?",
        "word": "Conversation"
    },

    {
        "story_id":"7",
        "inputs": 5,
        "category": "What is the name of the only country starting with the letter ‘Y’?",
        "word": "Yemen"
    },

    {
        "story_id":"8",
        "inputs": 6,
        "category": "What’s full of holes but can still hold liquid?",
        "word": "Sponge"
    },

    {
        "story_id":"9",
        "inputs": 6,
        "category": "European Country Name",
        "word": "France"
    },

    {
        "story_id":"10",
        "inputs": 11,
        "category": "What has four eyes but can’t see?",
        "word": "Mississippi"
    },
]


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run(debug=True)