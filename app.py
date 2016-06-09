from flask import Flask
import numpy as np
app = Flask(__name__)

userWordVector = {}

def sigmoid(score):
    return 2*(1/(1+np.exp(-score))-0.5)

def docToWordVector(bodyText):
    words = list(set(bodyText.replace("\n", "").replace(".", " ").replace("\"", "").split(" ")))
    words = filter(lambda a: a != '', words)
    wordVector = {}
    for word in words:
        wordVector[word] = sigmoid(bodyText.count(word))*len(word)
    return wordVector

def addDocVectors(v1, v2):
    for score in v2:
        if (v1.has_key(score)):
            v1[score] += v2[score]
        else:
            v1[score] = v2[score]


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/read", methods=["POST"])
def read():
    return "Something"

if __name__ == "__main__":
    placeholder = """WASHINGTON - Senator Bernie Sanders met with President Obama on Thursday and said afterward that he would do everything within his power to stop Donald Trump from becoming president - and would work closely with Hillary Clinton to make that happen.

After the meeting with Mr. Obama, which lasted more than an hour, Mr. Sanders gave no indication that he was ready to leave the race just yet, insisting that he would compete in next week's primary contest here in Washington. However, he made clear that party unity was on his mind.

"I will work as hard as I can, to make sure that Donald Trump does not become president of the United States," Mr. Sanders told reporters, saying the billionaire businessman "makes bigotry and discrimination the cornerstone of his campaign" and would be a "disaster" as commander in chief.

He said he would continue fighting for the issues that animated his campaign, including enhancing Social Security benefits, college affordability and restoring the nation's crumbling infrastructure.

"These are the issues that we will take to the Democratic National Convention in Philadelphia in July," Mr. Sanders said, declining to answer reporters' shouted questions about whether he would leave the race.

The visit came a day after the senator huddled with his team at his headquarters in Vermont to discuss the fate of his candidacy.

Mr. Sanders, who requested the meeting with the president, pulled into the White House grounds at 10:56 a.m. after stopping at a nearby Peet's Coffee for a scone. Mr. Obama and Mr. Sanders strolled down the colonnade next to the Rose Garden on their way into the Oval Office, chatting inaudibly and grinning broadly. Nearby, a thick line of cameras and cluster of microphones were assembled in the driveway outside the West Wing, where journalists peppered the Vermont senator with questions.

Mr. Obama was trying to negotiate, however gently, with him to exit the Democratic race without inflicting damage on efforts to unite the party.

"My hope is, is that over the next couple of weeks, we're able to pull things together," Mr. Obama said during a taping of an appearance on the "Tonight Show Starring Jimmy Fallon" on Wednesday in New York. "There's a natural process of everybody recognizing that this is not about any individual."

After his meeting with Mr. Obama, Mr. Sanders will head across town to see Senator Harry Reid, the Senate Democratic leader. While the two men are old friends, the conversation could be somewhat awkward as the minority leader has endorsed Mrs. Clinton and said publicly that Mr. Sanders should prepare to leave the race.

"Sometimes you just have to give up," Mr. Reid said last week.

Mr. Sanders was also scheduled to meet with Vice President Joseph R. Biden Jr. and Senator Chuck Schumer of New York while in Washington.

After Mrs. Clinton won Tuesday's California primary Mr. Sanders refused to quit the race, despite Mrs. Clinton's wide margin of victory and the fact that she had won enough pledged delegates for the nomination. But some of his supporters have started to walk away, prompting growing calls that it is time to bring the party together to defeat the presumptive Republican candidate, Donald J. Trump.

On Wednesday, Mr. Sanders sent out a fund-raising email asking for contributions of $2.70 and at 7 p.m. he will hold a rally outside of R.F.K. Stadium in Washington, where he will discuss his plans for getting big money out of politics and making public universities tuition-free."""

    addDocVectors(userWordVector, docToWordVector(placeholder))
    addDocVectors(userWordVector, docToWordVector(placeholder))
    print userWordVector
    # app.run()
