
import re

# Text of Romeo and Juliet
text = """
[SCENE II. Capulet’s Garden.]
[Enter Romeo.]
[Romeo.] He jests at scars that never felt a wound.
[Juliet appears above at a window.]
But soft, what light through yonder window breaks?
It is the east and Juliet is the sun!
Arise, fair sun, and kill the envious moon,
Who is already sick and pale with grief (5)
That thou her maid art far more fair than she.
Be not her maid, since she is envious;
Her vestal livery is but sick and green,
And none but fools do wear it. Cast it off.
It is my lady, O, it is my love! (10)
O that she knew she were!
She speaks, yet she says nothing; what of that?
Her eye discourses, I will answer it.
I am too bold: ’tis not to me she speaks.
Two of the fairest stars in all the heaven, (15)
Having some business, do entreat her eyes
To twinkle in their spheres till they return.
What if her eyes were there, they in her head?
The brightness of her cheek would shame those stars,
As daylight doth a lamp. Her eyes in heaven (20)
Would through the airy region stream so bright
That birds would sing and think it were not night.
See how she leans her cheek upon her hand
O that I were a glove upon that hand,
That I might touch that cheek! (25)
[Juliet.] Ay me!
[Romeo.] She speaks.
O, speak again, bright angel, for thou art
As glorious to this night, being o’er my head,
As is a winged messenger of heaven (30)
Unto the white-upturned wondering eyes
Of mortals that fall back to gaze on him
When he bestrides the lazy-puffing clouds
And sails upon the bosom of the air.
[Juliet.] O Romeo, Romeo! wherefore art thou Romeo?  (35)
Deny thy father and refuse thy name;
Or, if thou wilt not, be but sworn my love,
And I’ll no longer be a Capulet.
[Romeo.] [Aside.] Shall I hear more, or shall I speak at this?
[Juliet.] ‘Tis but thy name that is my enemy: (40)
Thou art thyself, though not a Montague.
What’s Montague? It is nor hand, nor foot,
Nor arm, nor face, nor any other part
Belonging to a man. O, be some other name.
What’s in a name? That which we call a rose (45)
By any other name would smell as sweet;
So Romeo would, were he not Romeo call’d,
Retain that dear perfection which he owes
Without that title. Romeo, doff thy name,
And for that name, which is no part of thee, (50)
Take all myself.
[Romeo.] I take thee at thy word.
Call me but love, and I’ll be new baptis’d;
Henceforth I never will be Romeo.
[Juliet.] What man art thou that, thus bescreened in night, (55)
So stumblest on my counsel?
[Romeo.] By a name
I know not how to tell thee who I am:
My name, dear saint, is hateful to myself,
Because it is an enemy to thee. (60)
Had I it written, I would tear the word.
[Juliet.] My ears have yet not drunk a hundred words
Of thy tongue’s uttering, yet I know the sound.
Art thou not Romeo, and a Montague?
[Romeo.] Neither, fair saint, if either thee dislike. (65)
[Juliet.] How cam’st thou hither, tell me, and wherefore?
The orchard walls are high and hard to climb,
And the place death, considering who thou art,
If any of my kinsmen find thee here.
[Romeo.] With love’s light wings did I o’erperch these walls, (70)
For stony limits cannot hold love out,
And what love can do, that dares love attempt:
Therefore thy kinsmen are no stop to me.
[Juliet.] If they do see thee, they will murder thee.
[Romeo.] Alack, there lies more peril in thine eye (75)
Than twenty of their swords. Look thou but sweet
And I am proof against their enmity.
[Juliet.] I would not for the world they saw thee here.
[Romeo.] I have night’s cloak to hide me from their eyes,
And, but thou love me, let them find me here; (80)
My life were better ended by their hate
Than death prorogued, wanting of thy love.
[Juliet.] By whose direction found’st thou out this place?
[Romeo.] By love, that first did prompt me to enquire.
He lent me counsel, and I lent him eyes. (85)
I am no pilot, yet, wert thou as far
As that vast shore wash’d with the furthest sea,
I should adventure for such merchandise.
[Juliet.] Thou knowest the mask of night is on my face,
Else would a maiden blush bepaint my cheek (90)
For that which thou hast heard me speak tonight.
Fain would I dwell on form; fain, fain deny
What I have spoke. But farewell compliment.
Dost thou love me? I know thou wilt say ‘Ay’,
And I will take thy word. Yet, if thou swear’st, (95)
Thou mayst prove false. At lovers’ perjuries,
They say, Jove laughs. O gentle Romeo,
If thou dost love, pronounce it faithfully:
Or if thou thinkest I am too quickly won,
I’ll frown, and be perverse, and say thee nay, (100)
So thou wilt woo: but else, not for the world.
In truth, fair Montague, I am too fond;
And therefore thou mayst think my ‘haviour light:
But trust me, gentleman, I’ll prove more true
Than those that have more cunning to be strange. (105)
I should have been more strange, I must confess,
But that thou overheard’st, ere I was ‘ware,
My true-love passion: therefore pardon me;
And not impute this yielding to light love
Which the dark night hath so discovered. (110)
[Romeo.] Lady, by yonder blessed moon I vow,
That tips with silver all these fruit-tree tops,—
[Juliet.] O, swear not by the moon, the inconstant moon,
That monthly changes in her circled orb,
Lest that thy love prove likewise variable. (115)
[Romeo.] What shall I swear by?
[Juliet.] Do not swear at all;
Or, if thou wilt, swear by thy gracious self,
Which is the god of my idolatry,
And I’ll believe thee.
[Romeo.] If my heart’s dear love— (120)
[Juliet.] Well, do not swear: although I joy in thee,
I have no joy of this contract to-night:
It is too rash, too unadvised, too sudden;
Too like the lightning, which doth cease to be
Ere one can say ‘It lightens.’ Sweet, good night! (125)
This bud of love, by summer’s ripening breath,
May prove a beauteous flower when next we meet.
Good night, good night! as sweet repose and rest
Come to thy heart as that within my breast!
[Romeo.] O, wilt thou leave me so unsatisfied? (130)
[Juliet.] What satisfaction canst thou have to-night?
[Romeo.] The exchange of thy love’s faithful vow for mine.
[Juliet.] I gave thee mine before thou didst request it:
And yet I would it were to give again.
[Romeo.] Wouldst thou withdraw it? for what purpose, love? (135)
[Juliet.] But to be frank, and give it thee again.
And yet I wish but for the thing I have:
My bounty is as boundless as the sea,
My love as deep; the more I give to thee,
The more I have, for both are infinite. (140)
I hear some noise within; dear love, adieu!
Anon, good nurse! Sweet Montague, be true.
Stay but a little, I will come again.
[Romeo.] O blessed, blessed night! I am afeard.
Being in night, all this is but a dream,
Too flattering-sweet to be substantial."""

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove stage directions
    text = re.sub(r'\[[^\]]+\]', '', text)
    # Remove character names
    text = re.sub(r'^\w+:', '', text, flags=re.MULTILINE)
    # Split into sentences
    sentences = re.split(r'[.!?]', text)
    return [s.strip() for s in sentences if s.strip()]

def analyze_sentiment(sentence, positive_words, negative_words):
    words = sentence.split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
positive_words = ['love', 'fair', 'good', 'happy', 'bright', 'sweet', 'virtuous', 'heaven', 'joy', 'peace', 'calm', 'casual', 'celebratory', 'cheerful', 'comforting', 'comic', 'compassionate', 'complimentary', 'conciliatory', 'confident', 'contented', 'delightful', 'earnest', 'ebullient', 'ecstatic', 'effusive', 'elated', 'empathetic', 'encouraging', 'euphoric', 'excited', 'exhilarated', 'expectant', 'facetious', 'fervent', 'flippant', 'forthright', 'friendly', 'funny', 'gleeful', 'gushy']
negative_words = ['hate', 'death', 'despair', 'sad', 'sorrow', 'weep', 'wrong', 'hell', 'tyrant', 'rage', 'apathetic', 'apprehensive', 'belligerent', 'bewildered', 'biting', 'bitter', 'blunt', 'bossy', 'cold', 'conceited', 'condescending', 'confused', 'contemptuous', 'curt', 'cynical', 'demanding', 'depressed', 'derisive', 'derogatory', 'desolate', 'despairing', 'desperate', 'detached', 'diabolic', 'disappointed', 'disliking', 'disrespectful']

explanation = """
Sentiment Analysis of Shakespeare's 'Romeo and Juliet'

This script performs a basic sentiment analysis on a scene from Shakespeare's 'Romeo and Juliet.'
The approach taken here is a simple word-based scoring method that does not rely on any machine learning models.

Method:

1.  Preprocessing: The script first preprocesses the text by converting it to lowercase, removing stage directions and character names, and splitting it into individual sentences.

2.  Word Lists: Two lists of words are used: one containing positive words and another containing negative words. These lists were compiled from various online sources.

3.  Scoring: Each sentence is analyzed by splitting it into words. A score is calculated for each sentence by incrementing a counter for each positive word and decrementing it for each negative word.

4.  Classification: Based on the final score, each sentence is classified as 'Positive' (score > 0), 'Negative' (score < 0), or 'Neutral' (score = 0).

This method is a straightforward way to get a basic understanding of the sentiment of a text. However, it has limitations. It does not account for sarcasm, irony, or the context in which words are used. For a more nuanced and accurate sentiment analysis, more advanced NLP techniques would be required.
"""

print(explanation)

sentences = preprocess_text(text)
for sentence in sentences[:20]:  # Analyze more sentences
    sentiment = analyze_sentiment(sentence, positive_words, negative_words)
    print(f"Sentence: '{sentence}'\nSentiment: {sentiment}\n")
