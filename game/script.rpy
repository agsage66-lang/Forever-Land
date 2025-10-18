# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define thalia = Character("Thalia", color = "#f27d83")

define friend = Character("Thalia's Friend")

define ailon = Character("Ailon")

define ivania = Character("Ivania")

define phobion = Character("Phobion")

#flags

default phobianJealosly = False

default meetIvania = False

#image control

layeredimage ailon :
    always: 
        "ailon_base"

    group expressions :
        attribute idle default:
            "ailon_normal"
        attribute surprise:
            "ailon_surprise"
        attribute surpriserosto:
            "ailon_surpriserosto"
        attribute smug:
            "ailon_smug"
        attribute blush:
            "ailon_blush"
        attribute sad:
            "ailon_sad"
        attribute shadow:
            "ailon_shadow"
        attribute side:
            "ailon_side"
        attribute smug:
            "ailon_smug"
        attribute strees:
            "ailon_stress"
        attribute sweet:
            "ailon_sweet"
        attribute sweetsmile:
            "ailon_sweetsmile"
        attribute verymad:
            "ailon_verymad"
        attribute verysurprise:
            "ailon_verysurprise"
        attribute veryworry:
            "ailon_veryworry"
        attribute worry:
            "ailon_worry"

layeredimage friend :
    always: 
        "friend_a"

    group expressions:
        attribute smile default:
            "friend_smile"
        attribute blush:
            "friend_blush"
        attribute surprise:
            "friend_surprise"
        attribute tired:
            "friend_tired"
        attribute worry:
            "friend_worry"

#transforms

transform smaller: #you can call it what ever you want 
    zoom 0.90
    yalign 1.0

label start:

    #======================== part 1 ================================
    scene bg coffeeshop

    play music "Buy Something!.mp3"


    "The day is just perfect, clear skies and mild weather to wear any mix of either winter or summer wear."

    "The morning in this particular store was slow, but for the two friends gossiping at the table."
    
    show thalia idle at left, smaller
    show friend at right
    with dissolve
    
    friend "Anyhow, you still haven’t told me how the date was…"

    show thalia sparkle

    thalia "I was so great! Like, amazing, he is pretty quiet, but those eyes~ dreamy."

    show thalia uwu

    thalia "He was very quiet, but truly I couldn’t get enough for just one date, especially his eyes. I wanna look at them again."

    friend "Sounds like he has you hooked…"

    show thalia convencida

    thalia "On the other way around, I have him hooked!"

    friend "It’s not what it sounds like it…"

    show thalia thinkblush

    thalia "Oh shut up… I played it cool"

    "Outside a well-dressed man with a calm, serene expression walks towards the store. Thalia quickly hides their face and whispers."

    show thalia 0
    
    thalia "OMG, it’s him! He is coming to this store!"

    friend "Did you invite him?"

    thalia "No… do you think it’s like fate?! We meet again, like boom! Sparks!"

    friend "Calm down, you have to play it cool. You're going to talk to him?"

    show thalia thinking

    thalia "Maybe…"

    show friend at center

    "The man walks in the store, his calm demeanor and presence seem to fill the room with ease, slowly he makes his way to the cashier."

    ailon "One coffee, black, large with cream."

    "His voice sounded like a gentle breeze when spoken, clear to understand and pleasant. He seemed blissfully unaware, and ultimately he simply stood patiently for his order."
    

    show friend at right

    show thalia convencida

    thalia "I’m gonna go talk to him."

    friend "Don’t look too desperate you might scare him."

    hide friend with dissolve

    "Thalia took a few steps closer to where the man stood."

    show thalia idle

    show ailon idle at right, with dissolve
    
    thalia "Ailon?"

    "He turned his head around and his calm expression changed to a soft smile, his eyes were the most attractive feature, like a pool of silver hinting blue they almost seemed unnatural, but mesmerizing."

    ailon "Hello Thalia, how unexpected."

    show thalia 0

    thalia "I know right, we just saw this café we’ve never been before and wanted to try."
    
    ailon "Well I come here almost every day it’s a nice place."

    show thalia satisfied

    thalia "Oh really that’s so nice… than I’m glad I chose to come here."


    show thalia nervous

    menu choice1 :
        "There a moment of this weird silence as Thalia thinks about what to say."
        "Ask why this store":
            jump choice1_A
        "Ask if he is free late":
            jump choice1_B

    label choice1_A:
        thalia "But hey… is there a reason you like this shop in particular?"
        
        show thalia o
        
        ailon "Well someone I knew opened this store, a long time ago, it reminds me of them…"

        show thalia shock

        thalia "Oh im sorry, was it a bad memory?"

        show thalia o

        ailon "No no, it was simply a bit of nostalgia." 

        "His smile is clear of an old memory but hides a slight sadness."

        ailon "But it was fortunate to meet you again today… I was thinking if you wanted to go somewhere again… if you want to"

        show thalia shock

        thalia "Oh… oh… oh!!!!"

        show thalia shockblush

        thalia "Yes I’d like to very much, I’m free even!"
        
        jump choice1_END
    
    label choice1_B:

        show thalia nervous

        thalia "After this, are you doing anything? If you are not, I’d love for a… second date maybe…"

        "He looks puzzled the surprised, a smile comes around his features lighting up the room."

        ailon "I’m glad you asked, I would be willing yes."

        show thalia happy

        thalia "Are you free today maybe? I wasn’t doing much, so I could go out this afternoon even!"

        ailon"Well… (his thoughts seem to drift for a moment but sure enough he returns with an awnser) I could yes."

        show thalia idle

        thalia"Since I chose last time do you wanna pick a place?"

        jump choice1_END

    label choice1_END:
        
    ailon "There is an amusement park here, Foreverlands, I happen to, well work there… and can get us in no problem."

    show thalia happy

    thalia "That sounds so cool, who knew I would know someone that well connected."

    ailon "Then when?"

    show thalia idle

    thalia "Oh right right… (she glances at her friend) maybe two hour in the main gate? I don’t wanna leave my friend just like this."

    ailon "That is is thoughtful of you… I do think however she might be a bit upset already."

    "Friend A has a sweet facade and gives a wave in response but Thalia know she will get an earful for ditching her over a date."

    thalia "I’ll see you there if I live through this."

    ailon "I sure hope you do."
   
    #======================== part 2 ================================

    scene bg parknoon
    show thalia convencida at left, smaller
    
    play music "one_0.mp3"

    with dissolve

    "The entrance to the park isnt as packed as in the mornings, most people already went in earlier in the day, however it doesn't stop a line from forming."   
    
    "Beyond the painted walls and decorated fences one can see the rollercoasters tracks, fabricated mountains and one of the largest ferries wheel."

    "There are various sounds of laughter and chatter that mix around the smell of fresh cooked popcorn and baked sweet that can make one flutter with anticipation."

    "Thalia is waiting beneath a small shade in the sidewalk, because even with the nice weather, staying in the sun is asking for a sun burn."

    "She can barely contain the smile across her face, even after getting a bi of scolding by her friend, she more than wished her luck on this date."

    "She was in the middle of talking to herself as if practicing flirts."

    show thalia sparkle

    thalia "So are you bringing me to the park because you wanted to do funny business with me?!"

    show thalia thinkblush

    thalia "no no… thats to forward and too weird."

    show ailon idle at right, with dissolve

    "Ailon comes into her field of view from the crowd close to the gate"

    show thalia shockblush

    "Thalia tries to hide a bit of the embarrassment from the attempted flirt as he approaches"

    show thalia o

    ailon "I hope you didn't wait long in this sun… you looked like you were talking to someone did i interrupt?"

    show thalia nervous

    thalia "No… i … was… well… just talking a bit to myself you know? making some mental notes… I remenber things better when i say them outloud!"

    show thalia shock

    ailon "Should I speak the whole day so you will remember?"

    show thalia shockblush

    "Thalia blushes with the unexpected comeback, and his calm way of saying it, just made her feel fluttery."

    ailon "But then come on we should head in, it might not look like it but its cooler in the park."

    show thalia happy

    thalia "Right!"

    "Thalia follows close to Ailon, as they both walk to the entrance, one of the employees open a side gate and he gestures so she follows, and they step into the park."

    "When they walk in she can feel a cooler breeze, and inside is full of color and people, most are just chatting from one ride to next, some are looking at the stores."

    "this part of the park looks like a small village, foreverlands, is mostly this medieval western fantasy themed, even the staff are either dressed as knights or peasants."

    "Thalia had been there before but not enough to remember most of it."

    show thalia o

    thalia "Oh my god it does feel so fresh in here, how did u know."

    "We keep so fan well positioned to help the airflow."

    show thalia 0

    thalia "We… wait you work here?! is that why they let us in on the side?"

    ailon "Well… that’s…"

    "Thalia had a moment of shock as she thinks of the possibility and loudly asks."

    show thalia shock

    thalia "Wait, do you OWN FOREVERLANDS?!"

    ailon "Shhhhhh (he gets closer as if to gesture her to bit less scandalous about it)"
    
    ailon "I don’t own, per say… I am just the major shareholder"

    thalia "You say that like it isn’t any less amazing!!"

    show thalia shinyeyes

    thalia "Do you get to go on the rides whenever you want? Do you have an infinite supply of popcorn? Can you close the park if you wanted to?"

    show thalia embarrased

    thalia "Oh… am I talking to much…"

    "Ailon had to hold a bit of his laughter but he managed to be composed enough to say "

    ailon "No but you are very loud."
    
    "Thalia looked around to see some people confused by all the noise and some curious, is not everyday you see the owner of the park"

    "She gets slightly flustered but also guilty"

    "Thalia grabs Ailons hand dragging him, he almost trips and running she says"

    show thalia shout

    thalia "Sorry I’ll make it up to you!"

    menu choice2: #Carnival-Choice
        "What should we do now?"
        "Drags Ailon to the old tales area":
            jump choice2_A
        "Drag Ailon to a ride":
            jump choice2_B
    
    label choice2_A:
        
        show thalia pouts

        "Thalia runs towards the most thematic part of the park"

        "There are less rides in this parts but many more stores, plays and games that are supposed to more closely resemble various old settlements" 

        "Various thematic areas are skillful placed to each be their own separate area, there are, western, eastern, egipician, Nordic and even some pre historic theme"

        show thalia  o

        "Thalia's stops to look around an intersection of these areas"

        show thalia happy

        thalia "This is so cool, it’s like miniature museums in here (she looks around trying to decide where she wants to go first)."

        thalia "Do you have any favorites?"

        ailon "Well…not really but this area as a whole is one I take a personal attachment to"

        show thalia o

        thalia "Oh? Are you really into history?"

        ailon "You could say that yes, all of those places once were the worlds to various civilizations and different cultures."

        ailon "They each had even their own way of seeing our world never mind the language, most are unique in their respective ways."

        "Ailon stops as he sees Thalia is starring at him"

        ailon "Sorry did I say something to boring?"

        show thalia satisfied

        thalia "It was the most I seen you speak I was very interested!"

        thalia "You almost like a teacher… say I never asked but how old are u? To be all like a grandpa on history"

        ailon "(He puts a finger on his lips) Can’t say, I stoped counting"

        show thalia pouts

        thalia "But birthday’s are so fun! (She pouts)."

        show thalia happy

        "They both laugh at this "

        "Something cached Thalia's attention, in a tribal tent there was this comical, likely costume lady, with cards and lots of feathers."

        show thalia o

        thalia "Is that a card reader?"

        ailon "Yes, her name was Ivania"

        thalia "I thought tribal readers did like with bones and smoke not cards (she laughs)"


        thalia "I’m gonna give it a try anyway, come on!"
 
        "Ailons seems to try and grab her hand, but Thalia slips and goes straight inside the tent"

        scene bg tent

        show thalia at smaller

        show thalia satisfied

        "There is a faint smell of oil, and a small pillow to kneel on, so she does and looks at the woman"

        "The woman named ivania seems just a bit older then her, she is in a full costume, making her features a bit stiff, and her whole body slightly bigger"

        "Thalia wondered if it was stuffy in there, or why wasn’t it easier to just dress up instead of a full suit"

        ivania "Welcome wonderer (her mouth moved slightly as she spoke, it was very cool how she could move like that, but perhaps just a bit stiff)"
 
        show thalia shinyeyes

        thalia "So cool you can move your mouth!"

        ivania "I can also tell you about your future, do you want to unmask your destiny?"

        thalia "I do!"

        ivania "Ivania pull out from the side five cards, but they weren’t the size of normal playing cards, they were slightly bigger then a hand."

        ivania "She then laid them in front of Thalia, a bit of smoke rose from the corners."

        "Ailon walked up to the corner of the tent but stood outside, Thalia was to focus to notice his face, as he seemed uneasy."

        ivania "I will now begin with a sight of the past"

        "She took the first card and put it in a pot, with one finger she seemed to draw inside."

        ivania "Time itself follows you, closer then u think"

        " she puts down a card with a sketch of a clock over a feminine figure in a red tinture"

        ivania "Now for the sight of your present"

        "(She does the same thing with the second card)"

        "(She puts down a big heart and many arrows)"

        ivania "Love is pulling in either direction it either be your piety or kindness that will take you forward."

        "(She picks up the third)"
        "(After drawing she says before putting it down)"

        ivania "You will see the end of your current world."

        "(The card shows a broken bridge overlooking a view)"

        show thalia o

        thalia "Is that bad?"

        "Ivania picks both of the last cards, she quickly draws on both, squeezing them together, she says in a whisper"

        ivania "It will depend in where will the dagger land."

        "(She shows almost identical cards, on one is a woman one is man, and a black dagger is embedded in both)"

        "Thalia has only a second to see both cards, before she is pulled by Ailon."

        show thalia shockblush

        ailon "She is playing to make you believe disaster, it alwaysallways to make a shock, she did that all the time!"

        "Thalia let her self be pulled for two reasons, the cards and words danced in her mind but so did the fact the Ailon was holding her hand, she blushed."
        
        "Yet a strange feeling also began to emerge inside."

        $ meetIvania = True

        jump choice2_END

    label choice2_B:
        "It isn’t very far off from the first roller coaster, there is a bit of line."

        show thalia idle

        thalia "So have you already gone in all the rides?"

        ailon "I have, yes."

        show thalia pouts

        thalia "(She pouts) oh so it won’t be so fun if you already know… but do you still want to?"

        ailon "They are made to be fun, I don’t mind going again if that’s what you want. (He smiles gently)"

        show thalia uwu

        "The smile feels Protagonist with some butterflies, his smile is so composed, that you could take a picture from any angle and it would look great, she thinks that at least."

        show thalia shock

        thalia "Say, since you own this place… could we skip ahead? (She says in a bit of a whisper)"

        ailon "I did not take for a rule breaker miss protagonist…"

        show thalia sparkle
 
        thalia "(She fakes being hit by a knife) you got me I was a bad girl (she laughs a bit)."

        ailon "I guess a bit of bending can’t hurt."

        show thalia uwu

        "Ailon takes protagonist by the hand up towards the front of the line"

        "Her heart pounds like a child on Christmas Eve, she kind of did that herself before but having him do it made her happy"

        show thalia idle

        "He talked real quick to one of the employees, they let both walk in, some people looked at them weird but perhaps they just had a fast pass"

        show thalia happy

        "The ride was fast, it was supposed to be like eletricity traveling across lightbulbs."

        "They both made it out and Thalia said."

        thalia "It was almost a light show, everything was so fast!"

        ailon "So it was fun?"

        show thalia shinyeyes

        thalia "Real real fun! What next? You wanna choose?"

        ailon "I have a feeling you will know best"

        thalia "Than this way! (She grabs his hand with enthusiasm)"

        hide thalia 
        
        hide ailon

        "They both spend some time from ride to ride."

        show thalia idle

        show ailon idle

        "Eventually Ailon asks for a moment to go to the toilet, so protagonist waits."

        "While she waits one of the characters, a figure that resembles a mosquetire approaches and says."

        show thalia 0

        "???" "Are you a fine lady on your own?"

        show thalia happy

        thalia "It seems not any more sir (she makes a fancy gesture)"

        "She can she it is a full suit, she imagines if it isn’t hot in there"

        "It’s also very sophisticated, it looked cartoonish enough to be abstract but can also move its mouth it a robotic manner"

        show thalia idle

        phobion "I was Knight Phobion, fine my lady!"

        show thalia o

        phobion "Say have you walk this parts with he?"

        show thalia confused

        thalia "(She is puzzled at first) with he?"

        phobion "The love of those in the park, most of us were here for him, I saw thou for afar."

        show thalia shock

        thalia "(She is again puzzled but figures out) oh you mean Ailon like… oh my god he is your boss right?"

        phobion "He was many to us part of us, now he seeks you."

        show thalia 0

        thalia "You mean you think he likes me? (She gets a bit flustered but also confused at his speech)"

        menu choice3: #know more
            phobion "I believe so lady, but you should seek not his path."
            
            "What do you mean? I don’t get it?":
                jump choice3_A
            "Oh so you jealous of us?":
                jump choice3_B
            
        label choice3_A:

            show thalia confused

            thalia "What do you mean? I don’t get it?"

            phobion"You need know about his past love, he won’t let you see, but you must see."

            show thalia o

            thalia "I don’t much care about his Exs, I have a few too."

            phobion "But they never left him, for this is land is forever"

            show thalia shockblush

            "A hand crosses around her and it’s Ailon hugging her from behind"

            show thalia uwu

            "Thalia had to concentrate not no melt in a puddle, but she couldn’t contain her smile, to her he was distant but now so close"

            ailon "Phobion we talked before and you can’t scare my dates like this"

            thalia "You said date… (she whispers softly)"

            phobion "You are right my loved Ailon, I was not chivalrous with lady, I’ll be of leave"

            show thalia confused

            ailon "But get your suit checked out, I see some errors."

            phobion "My pleasure!"

            "Phobion walks away."

            "He than turns protagonist around, his face a mixture of worry and embarrassment."

            ailon "I bet he said some weird things… he never really got over"

            show thalia o

            thalia "So he was an Ex…"

            ailon "I’m glad you got it, then… let’s walk around some more."

            show thalia satisfied

            thalia "Okay!"

            show thalia confused

            "When the initial shock wore off she looked to see if there was a trace of Phobion, she didn’t" 

            "Though outside she was happy as a butterfly she also thought it was very weird and she wanted to talk more to Phobion"

            jump choice3_END

        label choice3_B:

            $ phobianJealosly = True

            show thalia incomodada

            thalia "Oh so you jealous of us?"

            phobion "I simply wanted to…."

            show thalia angry

            thalia "What to ruin a date? (She says a bit angry) I finally got him to enjoy a good time and u come between? I can make him happy enough thank you very much!"

            phobion "(Lifts up a hand as if to talk back) I… will let you threat thy path."

            "Phobion walks away, and soon Ailon comes around looking at Phobion."

            ailon "Did he come talk you?"

            "Yeah he was being mean… you shouldn’t hire your exs you know? (She laughs a bit)"

            show thalia incomodada

            ailon "I… well… I’m glad you think so… I’ll have to talk to him afterwards."

            show thalia sparkle

            thalia "I wouldn’t worry too much (she grabs his hand and looks with sparkling eyes) I know I like you I just have to make sure you like me back~"

            "Protagonist begging screaming internally, asking if she was to forwards, maybe to cringe?! Could he like her back."

            "Ailon gave in return smile and blushed cheeks."

            ailon "Well I won’t tell u yet…"

            show thalia happy

            "There is a sweet air between the two"

            "Though Protagonist doesn’t see it, to chaotic her mind is there is a deep sadness forming in Ailons eyes, as if he is reading again a story he knows the end of it"

            "Both continue on their park adventure."
            
            jump choice3_END

        label choice3_END:
            jump choice2_END
    
    label choice2_END:

    scene bg parknigth

    show thalia at small

    show thalia idle at left

    show ailon at right

    if (phobianJealosly):
        jump part3b

    "They continued on to try other things, Mostly protagonist was adventuring around Foreverland, asking about the rides, and the different areas of the park."

    "The hours went by, the sun went down, and the lights came on, it gave a more mistic vibe to the whole place."

    "There were still many people around, but perhaps now most were tired from a day of playing around so it seemed more slow and calm."

    thalia "This place is so cool! It’s so different at night right?"

    "She was more stating than asking so Ailon kept quite, he didn’t seem tired but a bit distracted."

    thalia "Where did this come from anyway?"

    ailon "(He was a bit confused) what you mean?"

    thalia "This park, its theme park, where did the ideia come from? Was it yours?… maybe your dad’s? This park has been here a while right?"

    ailon "It has yes, almost two hundred years the park has, but it wasn’t this big for a while."

    thalia "That’s so cool! So it does belong to your family who had the ideia?"

    "Ailon seemed to shift a bit as if thinging, maybe a little to hard on the subject but then he spoke."

    ailon "My grandpa… he wanted to make a place for people he knew."

    thalia "So he made a theme park? Not a hotel or maybe even a bar where he could have them around?"

    ailon "He… wanted to make them feel at home, that’s why he… made all these different areas."

    thalia "Oh! So there were all foreigners?"

    ailon "Something like that…"

    thalia "Your grandad seems sweet then."

    ailon "(Playfully he said) so you were after my grandad not me? How scandalous!"

    thalia "(Joking) oh now I have been exposed! (She holds her hands to her chest)"

    ailon "Should have known you like them old!"

    thalia "They do have more experience, so maybe it’s for the best."

    ailon "Is that why you take a interest on me? Cause you think I’m old?"

    thalia "(She blushed a bit but said confidently) i don’t know you haven’t told me… but you do feel old…"

    thalia "(She rapidly tries to save from calling this young man old) old in the good way I mean! Like that is confortable to be around you…"

    "Ailon seems a bit surprised but happy by the statement."

    menu part3choice:
        "Thalia blushes a bit while trying desperately to think how to change topics."

        "What do you like about me then? (She asks bluntly)":
            jump part3choice_a
        "Do you believe in destiny? Like the woman said?" if meetIvania:
            jump part3choice_b
        "Who was that guy anyway? He said some strange things." if not meetIvania:
            jump part3choice_c
    
    label part3choice_a:

        "Ailon looked at her  for a moment, his mind seemed to drift a bit "

        ailon "I guess… it would be your forwardness, i haven’t been one to begin things as of late, it’s refreshing."

        thalia "Everyone has bad times, you don’t need to feel so bad about."

        "Protagonist put a hand in his shoulder as if to comfort him, she saw him as someone older but now he seemed smaller"

        ailon "I am humbled by your words but I don’t know if I can even be in this type of relationship you imagine right now…"

        "Even by his words he seemed to lean a bit forward, she saw there was this faint hope in his eyes."

        "Thalia leaned a bit closer and gave him a kiss in the cheek "

        "He turned his eyes a bit shocked so she backed slightly embarrassed"

        thalia "(She said nervously) I’m sorry… maybe i shouldn’t have done that…"

        ailon "(He was blushing and also a bit nervously) I… no you… its okay, I just wasn’t ready can you give me a minute?"

        thalia "(She was shocked) then… maybe I should go home…"

        ailon "No no, stay… i just need a minute to get my mind in order… here."

        "He approached her, pulled her hand and gave her a card."

        ailon "You can use it to get something to eat around here if you are hungry… I’ll be back… just… don’t leave?"

        "He seemed genuinely confused in his feeling but his words seemed true"

        thalia "Okay… I’ll stay a bit."

        "He seemed relaxed and then nodded and walked away."

        "Protagonist sat in a bench close by the put her hands in her hair embarrassed mumbling. "

        thalia "Oh no… now I messed it up… I shouldn’t have… but he looked so sad…"

        "Suddenly a figure of a man in a hood came by and said in a soft voice"

        jump harryNapped

    label part3choice_b:
        
        thalia "You know… like what Ivania said."

        ailon "(He seemed a little frustrated when he heard the name) she was trying to scare you like I said, it a bad habit she has."

        thalia "But aren’t card readers supposed to tell truth on their cards."

        ailon "But she exaggerated, it’s a park afterall, it has to bring some emotion."

        thalia "(Doubtful) then why are you so mixed up trying to dismiss what she said?"

        ailon "Because I don’t wanna hurt you!"

        "She was shocked, it the first time she saw him raise his voice, it wasn’t a scream per say, but as low as he talked it was loud."

        ailon "Oh I’m sorry… i didn’t mean to scream."

        thalia "So you have a sensible side too… a bit childish too at that (she said smug)"

        ailon "What?"

        thalia "Every relationship is complicated, and sometime you hurt each other… you maybe older then me but I not naive like that."

        "Ailon looked surprised, he seems to expect something different, maybe rejection, but he got a response."

        thalia "So? You still wanna tell me the same?"

        ailon "It’s more complicated then that…"

        thalia "(She sighs) and they say woman are complicated…"

        "She walks up to Ailon pulls him and gives him a fast kiss on the lips."

        "Inside she was so nervous she could be shaking, but she was also a bit angry, and wanted to show him her commitment."

        "Ailon looked shocked, then embarrassed, then the embarrassment came back to protagonist as well, She turned around and said."

        thalia "There… you either liked it… or didn’t."

        "There a strange moment of silence, but it felt longer for both."

        "Protagonist got even more embarrassed and she felt like she wanted to disappear she was getting ready to run off when Ailon grabbed her hand."

        ailon "I need a minute… and I think you do to… meet at the central plaza later… and have this, anything you want. Its is my treat."

        "He handed protagonist a small card, then walked away."

        "She was very shocked still, was that a good sing? A bad one?"

        "She stood there a bit giddy and did not see a man approach her."
        "He was wearing a hood and said in a soft voice."

        jump harryNapped


        
    label harryNapped:

        "???" "Hey did he gave you a card?"

        thalia "What…"

        "???" "Ailon, did he give you a card?"

        thalia "Yeah he did…"

        "She stopped when she saw him pulling a gun, she thought about screaming there weren’t many people around but it was sure to draw attention."

        "But she was so surprised it was like her body froze in fear."

        "???" "You scream you die… you run you die…you will get up, stand next to me and walk, then you live… nod if you understood."

        "Protagonist mind began racing with the very ideas he just warned her against, but if he was crazy enough to try and pull this in a park full of people, she might die."

        "As natural as she could she got up slowly and he came around the side putting the gun behind her and hiding between them."

        thalia "What…. What you want from me?"

        "???" "I want you to fucking live, now walk to that employee exit on the left."

        "She was confused but did as she was told."

        "Protagonist walked and he followed right up to the door."

        "???" "Use the card to open the door."

        "Still scared she pulled out the card, passed on the scanner beside the door, and to her surprise it worked."

        "She heard a sight of relief, not from her but from the man he mumbled (it does work)."

        "He pushed her inside and closed the door behind them."
        
        jump part3end

    label part3choice_c:
    
        ailon "Who do you mean?"

        thalia "The one in the musketeer costume… Phobion I think seemed very well… you know."

        ailon "He was just jealous and a bit confused I’m sure."

        ailon "Why do you keep him in the park?"

        "Ailon seemed puzzled by the question, not as if he did know the answer but that he didn’t know how to tell her."

        thalia" Maybe I should talk to him? Get him to understand that he can’t butt in like that."

        ailon "You would stand up like that?"

        thalia "Only because he didn’t seem to want to be mean about it… I mean he wasn’t mean, he was trying to tell me something."

        ailon "Like what?"

        thalia "Just that you loved the people here… I think I was a bit confused too."

        "Ailon looked confused but then his face had a little more serious look, not in the threatening way but the determined look."

        ailon "Say Protagonist do you still wanna talk to him?"

        thalia "Maybe I mean… he seemed to want to say things, it’s important to listen to people."

        ailon "Then would you listen to this?"

        "Ailon pulls her a bit closer, protagonist gets flustered and he leans in as if asking"

        "She what, asking for a kiss, her heart beat real fast and she agreed "

        "He kissed her for only o moment, leaving her dovey with love, he too was somewhat flustered"

        ailon "I… would you rather think of this instead… I should prepare something then."

        "He a bit clumsy searched his clothes and pulled a card."

        ailon "Have this to buy something if you are hungry, or show that to the employees, if ya need me, I’m gonna need a moment."

        "He ran off before she could respond "

        "Her heart was beating so loud she could barely hear her own thoughts, but she could feel, besides the embarrassment and uneasiness."

        "She took a long breath, looked around and went to talk to one of the employees."

        thalia "Excuse me… I… I need to talk to Phobion."

        "I’m sorry Ma’am I don’t know what you mean."

        thalia "The musketeer Phobion… (she showed him the card) here can you take me to him."

        "The employee simply nodded in silence, and told her to follow."

        "She kept thinking about the kiss but this curiosity also was consuming her, so she was convicted to try her own path."

        "Both the employee and protagonist failed to notice a man following both, and he had been there a while."
        
        jump part3end
    
    label part3b:

        "Both Ailon and Protagonist go on a lot of rides, they almost get to ride all of them before they stop to rest a while"

        "Protagonist was feeling really happy but she didn’t know if Ailon was having the same amount of fun"

        "She saw him smile, talked to him, to her he did look handsome but it was making her somehow uncomfortable "

        "She also kept thinking back to that weird guy in the costume Phobion"

        thalia  "Ailon, why would you keep an Ex you have working here?"

        ailon "(He seemed slightly surprised by the question) what you mean by it?"

        thalia "Phobion he was trying to talk to me, to I think… not like you but why do keep him employed? Isn’t it uncomfortable?"

        ailon "Should I fire him because relationship, he can be good at his job…"

        thalia "Not good if he bothers our date! (She pouts)"

        "She is feeling something other than bother but she can’t quite place the feeling, so she looks at him to see what he says."

        ailon "You know… you are right… I should go give him a piece of mind."

        thalia "Now?"

        ailon "Well in case he comes bother us again."

        menu phobionHurt:
            "She was upset he was stepping away but happy he seemed to mind the date enough, and that somehow made her feel relieved."

            "Tell him if he bothers us again I’ll bite kick his butt":
                jump phobionHurtA
            "Why was he that hurt?":
                jump phobionHurtB

    label phobionHurtA:

        ailon "I’m just gonna talk to him not beat him."

        thalia "I know… but I’ll be bored without you here (she blinks her eyes as if making a charm)."

        ailon "Okay… then to make it up… this?"

        "He hands her a card."

        ailon "You should be able to get yourself anything you want."

        thalia "So you are buying me…?"

        "Ailon seemed to be upset by her words, he meant to take the card but she backed a bit."

        "Inside her she began to dislike that off the ground side of him, that arrogance he knew better."

        "She wanted to be petty."

        thalia "I didn’t say I wouldn’t take it."

        "Ailon seemed a bit sad by those words, she also began feeling a little bad by doing it."

        "He than turned his back and walked away."

        "Protagonist was left to think and began talking to herself ."

        thalia "I like him… but now he just seemed weird, I don’t know if I like that."

        "???" "Maybe you should find out what he is really doing."

        "She hadn’t noticed but a man in a hoodie was juts next to her."

        "She jumped at his sudden appearance."

        thalia "I’m sorry… do i know you?"

        "???" "No, but you don’t know Ailon either."

        "???" "He is hiding things from you."

        thalia "(She was curious enough to ask) like what?"

        "???" "That card does more than buy ya things, he just didn’t tell you."

        "The strange man gestures to an employee door"

        "Protagonist feels really skeptical, and a bit scared so she does as she is told"

        "To her surprise after passing the card the door opens and inside her suspicion sets"

        thalia "What now then?"

        "???" "Now we better go there before someone sees us. "

        "She goes in and the man follows closing the door behind."

        "Harry" "The name is Harry, lady… and u might need this."

        "From under his hood he hands Thalia a gun."

        jump part3end

    label phobionHurtB:

        ailon "It’s a long story… (he seemed sad)"

        "She saw a slight pain in his eyes, she walked to a bench and gestured."

        thalia "Well luckily we got time."

        "He looked at the bench next to her and hesitantly sat down"

        thalia "I was… maybe a bit mean… but I was upset but look sad did you too had a long time together."

        ailon "Yeah you could say that… but wasn’t the only one."

        "Thalia began to see that he seemed pained talking about it, perhaps way more the she expected."

        thalia "Maybe it’s still not the right moment to talk about it… but I’m glad you have shown it to me?"

        ailon "That I’m a mess."

        thalia "That you are human."

        "(She laughs a bit akward)"

        "I think… honestly that you are very handsome… but it’s good to see that you are soft."

        "Ailon looked at her still a bit hurt but slightly more composed and looking up to her in a soft tender look, almost inviting."

        "She leaned in and gave him a kiss."

        "I can be here for you… if you let me…"

        "Ailon didn’t say anything he seemed aloft and he blushed."

        "He stood up after a moment and handed her back a card."

        ailon "Buy something to eat… I’ll be back in a bit I need to clear my head."

        thalia "Did I…"

        ailon "No no… it’s more me you can rest easy, I’ll be back if you still here."

        "She hesitate but took the card."

        "Before she could say anything he left."

        "Thalia felt slightly awkward but relived she got to see a gentle and timid saúde of him, one that needed caring."

        "She didn’t notice a man in a hood getting close to her till he spoke."
        
        "???" "Do not scream… or you die."

        "She looked and saw that the figure was holding a gun up to her, there were people around but in the quiet corner no one paid much attention."

        "Protagonist was shocked she couldn’t scream if she wanted to, so she just held the card firmly. "

        "???" "You are going to get up, you won’t run or I’ll kill you… you are gonna come with me to that door, and you are gonna play it cool…. Nod if u understand."

        "Protagonist nooded, she wanted to run, she did want to scream, but what if he shot she thought."

        "She did as he told her, got up, next to him, she felt the gun touch her back, as he hid it between them, and he whispered."

        "???" "Walk to the door and swipe the card."

        "She again did just like he said, her head was spinning and she felt her hands cold."

        "When she reached the door, there was a beep, the door opened, he pushed her inside and lock the door behind them, no one saw a thing."

        jump part3end



    label part3end:

        
    label end:
    
    return
