# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define thalia = Character("Thalia", color = "#f27d83")

define friend = Character("Thalia's Friend", color = "#846FB7")

define ailon = Character("Ailon", color = "#A0B3BA")

define ivania = Character("Ivania", color = "#316374")

define phobion = Character("Phobion", color = "#316374")

define harry = Character("Harry", color = "#E5AE6E")

#flags

default phobianJealosly = False

default meetIvania = False

default harryNapped = False

default harryFriend = False

#image control

layeredimage thalia:
    always:
        "thalia_base"

    group expressions:
        attribute idle default:
            "thalia_idle"
        attribute bigopen:
            "thalia_bigopen"
        attribute bignoblush:
            "thalia_bignoblush"
        attribute angry:
            "thalia_angry"
        attribute confused:
            "thalia_confused"
        attribute convencida:
            "thalia_proud"
        attribute cutesmile:
            "thalia_cutesmile"
        attribute disgust:
            "thalia_disgust"
        attribute bigDisgust:
            "thalia_disgust2"
        attribute embarrased:
            "thalia_vergonha"
        attribute happy:
            "thalia_happy"
        attribute o:
            "thalia_littleopen"
        attribute nervous:
            "thalia_sideeye"
        attribute  pouts:
            "thalia_pouts"
        attribute satisfied:
            "thalia_smile"
        attribute shinyeyes:
            "thalia_shineeyes"
        attribute shout:
            "thalia_shout"
        attribute sparkle:
            "thalia_sparkle"
        attribute surprise:
            "thalia_surprise"
        attribute surpriseblush:
            "thalia_surpriseblush"
        attribute thinking:
            "thalia_think"
        attribute verysurprise:
            "thalia_verysurprise"
        attribute uwu:
            "thalia_uwu"

    group extras:
        attribute noeffect default:
            null
        attribute smallBlush:
            "thalia_blush2"
        attribute bigBlush:
            "thalia_blush"

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
        attribute sad:
            "ailon_sad"
        attribute side:
            "ailon_side"
        attribute smug:
            "ailon_smug"
        attribute stress:
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
        attribute smile:
            "ailon_smile"
        attribute o:
            "ailon_o"

    group extras:
        attribute noeffect default:
            null
        attribute blush :
            "ailon_blush"
        attribute shadow :
            "ailon_shadow"


layeredimage harry:
    always:
        "harry_idle"
    group expressions:
        attribute smile:
            "harry_smile"

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

transform lightFilter:
    matrixcolor TintMatrix("#7FA5F2")

transform shadowFilter:
    matrixcolor TintMatrix("#000000")

transform cardRight:
    yalign 0
    xalign 0.675

transform cardLeft:
    yalign 0
    xalign 0.325

transform flip:
    xzoom -1

transform reverseFlip:
    xzoom 1


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

    show friend blush

    friend "Sounds like he has you hooked…"

    show thalia convencida

    thalia "On the other way around, I have him hooked!"

    show friend worry

    friend "It’s not what it sounds like it…"

    show thalia thinking smallBlush
    thalia "Oh shut up… I played it cool"

    "Outside a well-dressed man with a calm, serene expression walks towards the store. Thalia quickly hides their face and whispers."

    show thalia bigopen
    
    thalia "OMG, it’s him! He is coming to this store!"

    show friend surprise

    friend "Did you invite him?"

    thalia "No… do you think it’s like fate?! We meet again, like boom! Sparks!"

    friend "Calm down, you have to play it cool. You're going to talk to him?"

    show thalia thinking bigBlush

    thalia "Maybe…"

    show friend tired

    "The man walks in the store, his calm demeanor and presence seem to fill the room with ease, slowly he makes his way to the cashier."

    ailon "One coffee, black, large with cream."

    "His voice sounded like a gentle breeze when spoken, clear to understand and pleasant. He seemed blissfully unaware, and ultimately he simply stood patiently for his order."
    
    show thalia convencida -bigBlush

    thalia "I’m gonna go talk to him."

    show friend tired

    friend "Don’t look too desperate you might scare him."

    "Thalia took a few steps closer to where the man stood."

    show thalia idle

    hide friend
    show ailon idle at right
    with dissolve
    
    thalia "Ailon?"

    show ailon surprise

    "He turned his head around and his calm expression changed to a soft smile, his eyes were the most attractive feature, like a pool of silver hinting blue they almost seemed unnatural, but mesmerizing."

    show ailon sweetsmile

    ailon "Hello Thalia, how unexpected."

    show ailon smile

    show thalia bigopen

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

        show ailon sad
        
        ailon "Well someone I knew opened this store, a long time ago, it reminds me of them…"

        show thalia verysurprise

        thalia "Oh im sorry, was it a bad memory?"

        show thalia o

        ailon "No no, it was simply a bit of nostalgia." 

        show ailon smile

        "His smile is clear of an old memory but hides a slight sadness."

        show ailon o

        ailon "But it was fortunate to meet you again today… I was thinking if you wanted to go somewhere again… if you want to"

        show thalia verysurprise

        thalia "Oh… oh… oh!!!!"

        show thalia verysurprise bigBlush
        show ailon sweet

        thalia "Yes I’d like to very much, I’m free even!"
        
        jump choice1_END
    
    label choice1_B:

        show thalia nervous

        thalia "After this, are you doing anything? If you are not, I’d love for a… second date maybe…"

        show ailon surprise

        "He looks puzzled the surprised, a smile comes around his features lighting up the room."

        show ailon smile

        ailon "I’m glad you asked, I would be willing yes."

        show thalia happy

        thalia "Are you free today maybe? I wasn’t doing much, so I could go out this afternoon even!"

        show ailon sweetsmile

        ailon"Well… (his thoughts seem to drift for a moment but sure enough he returns with an awnser) I could yes."

        show thalia idle

        thalia"Since I chose last time do you wanna pick a place?"

        jump choice1_END

    label choice1_END:

    show ailon smile    
        
    ailon "There is an amusement park here, Foreverlands, I happen to, well work there… and can get us in no problem."

    show thalia happy -bigBlush

    thalia "That sounds so cool, who knew I would know someone that well connected."

    show ailon o

    ailon "Then when?"

    show thalia idle

    thalia "Oh right right… (she glances at her friend) maybe two hours in the main gate? I don’t wanna leave my friend just like this."

    show thalia nervous

    ailon "That is is thoughtful of you… I do think however she might be a bit upset already."

    "Friend A has a sweet facade and gives a wave in response but Thalia know she will get an earful for ditching her over a date."

    thalia "I’ll see you there if I live through this."

    show ailon sweetsmile

    ailon "I sure hope you do."
   
    #======================== part 2 ================================

    scene bg parknoon

    stop music fadeout 1.0

    show thalia convencida at left, smaller
    
    play music "one_0.mp3"

    with dissolve
    
    "The entrance to the park isn't as packed as in the mornings; most people already went in earlier in the day, however, it doesn't stop a line from forming."

    "Beyond the painted walls and decorated fences one can see the rollercoasters tracks, fabricated mountains and one of the largest ferries wheel."

    "There are various sounds of laughter and chatter that mix around the smell of fresh cooked popcorn and baked sweet that can make one flutter with anticipation."

    "Thalia is waiting beneath a small shade in the sidewalk, because even with the nice weather, staying in the sun is asking for a sun burn."

    "She can barely contain the smile across her face, even after getting a bi of scolding by her friend, she more than wished her luck on this date."

    "She was in the middle of talking to herself as if practicing flirts."
    
    show thalia sparkle

    thalia "So are you bringing me to the park because you wanted to do funny business with me?!"

    show thalia thinking bigBlush

    thalia "no no… thats to forward and too weird."

    show ailon idle at right, with dissolve

    "Ailon comes into her field of view from the crowd close to the gate."

    show thalia verysurprise

    "Thalia tries to hide a bit of the embarrassment from the attempted flirt as he approaches."
    
    show thalia o

    show ailon smile

    ailon "I hope you didn't wait long in this sun… You looked like you were talking to someone. Did I interrupt?"

    show thalia nervous -bigBlush

    thalia "No… I… was… well… just talking a bit to myself, you know? Making some mental notes… I remember things better when I say them outloud!"

    show thalia shock

    show ailon sweetsmile

    ailon "Should I speak the whole day so you will remember?"

    show thalia verysurprise bigBlush

    "Thalia blushes with the unexpected comeback, and his calm way of saying it, just made her feel fluttery."

    show thalia thinking bigBlush

    show ailon smile

    ailon "But then come on we should head in, it might not look like it but its cooler in the park."

    show thalia happy smallBlush

    thalia "Right!"

    show thalia happy

    "Thalia follows close to Ailon as they both walk to the entrance; one of the employees opens a side gate, and he gestures so she follows, and they step into the park."

    "When they walk in, she can feel a cooler breeze, and inside is full of color and people; most are just chatting from one ride to the next, and some are looking at the stores."

    "This part of the park looks like a small village. Foreverlands is mostly this medieval western fantasy theme; even the staff are either dressed as knights or peasants."

    "Thalia had been there before but not enough to remember most of it."

    show thalia o -smallBlush

    thalia "Oh my god, it does feel so fresh in here. How did you know?"

    show ailon o

    ailon "We keep the fan well positioned to help the airflow."

    show thalia bigopen

    show ailon surprise

    thalia "We… wait you work here?! is that why they let us in on the side?"

    show ailon worry

    ailon "Well… that’s…"

    "Thalia had a moment of shock as she thinks of the possibility and loudly asks."

    show ailon surprise

    show thalia verysurprise

    thalia "Wait, do you OWN FOREVERLANDS?!"

    show ailon stress at center

    show thalia o

    ailon "Shhhhhh!"

    show thalia confused

    show ailon verysurprise blush at right
    
    ailon "I don’t own it, per say… I am just the major shareholder."

    show thalia bigopen

    show ailon idle -blush at right

    thalia "You say that like it isn’t any less amazing!!"

    show thalia shinyeyes

    show ailon smile

    thalia "Do you get to go on the rides whenever you want? Do you have an infinite supply of popcorn? Can you close the park if you wanted to?"

    show thalia embarrased

    thalia "Oh… am I talking to much…"

    "Ailon tried and failed to hold back his laughter, but he managed to be composed enough to say."

    show ailon sweetsmile

    ailon "No but you are very loud."

    "Thalia looked around to see some people confused by all the noise and some curious; it is not every day you see the owner of the park."

    "She gets slightly flustered but also guilty."

    show ailon surprise blush

    "Thalia grabs Ailon's hand, dragging him; he almost trips, and while running, she says."

    show thalia shout

    show ailon surprise

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

        show thalia o

        "Thalia's stops to look around an intersection of these areas"

        show thalia happy

        show ailon smile

        thalia "This is so cool, it’s like miniature museums in here (she looks around trying to decide where she wants to go first)."

        thalia "Do you have any favorites?"

        ailon "Well…not really but this area as a whole is one I take a personal attachment to"

        show thalia o

        thalia "Oh? Are you really into history?"

        show ailon side

        ailon "You could say that yes, all of those places once were the worlds to various civilizations and different cultures."

        show ailon smile

        ailon "They each had even their own way of seeing our world never mind the language, most are unique in their respective ways."

        "Ailon stops as he sees Thalia is starring at him."
        
        show ailon worry blush

        ailon "Sorry did I say something to boring?"

        show thalia satisfied

        thalia "It was the most I seen you speak I was very interested!"

        thalia "You almost like a teacher… say I never asked but how old are you? To be all like a grandpa on history"

        show ailon smile -blush

        ailon "(He puts a finger on his lips) Can’t say, I stoped counting"

        show thalia pouts

        thalia "But birthday’s are so fun! (She pouts)."

        show ailon sweet

        show thalia happy

        "They both laugh at this."

        "Something cached Thalia's attention, in a tribal tent there was this comical, likely costume lady, with cards and lots of feathers."

        show thalia o

        thalia "Is that a card reader?"

        show ailon smile

        ailon "Yes, her name was Ivania."

        show thalia smile

        thalia "I thought tribal readers did like with bones and smoke,not cards."

        show ailon surprise

        thalia "I’m gonna give it a try anyway, come on!"

        show ailon worry
 
        "Ailons seems to try and grab her hand, but Thalia slips and goes straight inside the tent"

        scene bg tent

        stop music fadeout 1.0

        show thalia satisfied at smaller, left
        with dissolve

        play music "wind_chimes_loop_3.ogg"

        "There is a faint smell of oil, and a small pillow to kneel on, so she does and looks at the woman"

        show ivania idle at right with dissolve

        "The woman named ivania seems just a bit older then her, she is in a full costume, making her features a bit stiff, and her whole body slightly bigger"

        "Thalia wondered if it was stuffy in there, or why wasn’t it easier to just dress up instead of a full suit"

        ivania "Welcome wonderer (her mouth moved slightly as she spoke, it was very cool how she could move like that, but perhaps just a bit stiff)"
 
        show thalia shinyeyes

        thalia "So cool you can move your mouth!"

        ivania "I can also tell you about your future, do you want to unmask your destiny?"

        thalia "I do!"

        show thalia o

        ivania "Ivania pull out from the side five cards, but they weren’t the size of normal playing cards, they were slightly bigger then a hand."

        ivania "She then laid them in front of Thalia, a bit of smoke rose from the corners."

        "Ailon walked up to the corner of the tent but stood outside, Thalia was to focused to notice his presence, as he seemed uneasy."

        ivania "I will now begin with a sight of the past."

        "She took the first card and put it in a pot, with one finger she seemed to draw inside."

        show thalia at lightFilter , left

        show ivania at lightFilter

        show cards time at top, smaller with dissolve

        ivania "Time itself follows you, closer thenyoy think."

        "She puts down a card with a sketch of a clock over a feminine figure in a red tinture"

        ivania "Now for the sight of your present"

        "(She does the same thing with the second card)"

        "(She puts down a big heart and many arrows)"

        show cards heart

        ivania "Love is pulling in either direction it either be your piety or kindness that will take you forward."

        "(She picks up the third)"
        "(After drawing she says before putting it down)"

        ivania "You will see the end of your current world."

        show cards bridge

        "(The card shows a broken bridge overlooking a view)"

        thalia "Is that bad?"

        "Ivania picks both of the last cards, she quickly draws on both, squeezing them together, she says in a whisper"

        ivania "It will depend in where will the dagger land."

        "(She shows almost identical cards, on one is a woman one is man, and a black dagger is embedded in both)"

        show cards woman at cardRight
        show anothercards man at top, smaller, cardLeft with dissolve

        "Thalia has only a second to see both cards, before she is pulled by Ailon."

        hide cards 

        hide anothercards

        with dissolve 

        hide thalia

        hide ivania

        show ailon worry at left, flip 

        show thalia bigopen bigBlush at center , smaller

        show ivania idle at right

        with dissolve

        ailon "She is playing to make you believe disaster, it alwaysallways to make a shock, she did that all the time!"

        show thalia uwu

        "Thalia let her self be pulled for two reasons, the cards and words danced in her mind but so did the fact the Ailon was holding her hand, she blushed."
        
        "Yet a strange feeling also began to emerge inside."

        $ meetIvania = True

        jump choice2_END

    label choice2_B:
        "It isn’t very far off from the first roller coaster; there is a bit of a line."

        show thalia idle

        thalia "So have you already gone on all the rides?"

        show ailon smile

        ailon "I have, yes."

        show thalia pouts

        thalia "(She pouts) Oh, so it won’t be so fun if you already know… but do you still want to?"

        ailon "They are made to be fun; I don’t mind going again if that’s what you want. (He smiles gently.)"

        show thalia uwu

        "The smile feels Protagonist with some butterflies, his smile is so composed, that you could take a picture from any angle and it would look great, she thinks that at least."

        show thalia verysurprise

        show ailon idle -blush

        thalia "Say, since you own this place… could we skip ahead? (She says in a bit of a whisper)"

        show ailon sweetsmile

        ailon "I did not take for a rule breaker miss protagonist…"

        show thalia sparkle
 
        thalia "(She fakes being hit by a knife) you got me I was a bad girl (she laughs a bit)."

        ailon "I guess a bit of bending can’t hurt."

        show thalia convencida

        "Ailon takes protagonist by the hand up towards the front of the line"

        "Her heart pounds like a child on Christmas Eve, she kind of did that herself before but having him do it made her happy"

        show thalia idle

        show ailon o

        "He talked real quick to one of the employees, they let both walk in, some people looked at them weird but perhaps they just had a fast pass."

        show thalia satisfied

        show ailon sweetsmile

        "The ride was fast, it was supposed to be like eletricity traveling across lightbulbs."

        "They both made it out and Thalia said."

        thalia "It was almost a light show, everything was so fast!"

        show ailon smile

        ailon "So it was fun?"

        show thalia shinyeyes

        thalia "Real real fun! What next? You wanna choose?"

        ailon "I have a feeling you will know best"

        thalia "Than this way! (She grabs his hand with enthusiasm)"

        hide thalia 
        
        hide ailon

        with dissolve

        "They both spend some time from ride to ride."

        "Eventually Ailon asks for a moment to go to the toilet, so protagonist waits."

        hide ailon

        "While she waits one of the characters, a figure that resembles a mosquetire approaches and says."

        show thalia o at smaller, left with dissolve

        "???" "Are you a fine lady on your own?"

        show thalia happy

        show phobion idle at right

        with dissolve

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

            phobion "But they never left him, for this is land is forever."

            show thalia bigopen bigBlush at center 

            show thalia at smaller

            show ailon o at left, flip

            "A hand crosses around her and it’s Ailon hugging her from behind."

            show thalia uwu

            "Thalia had to concentrate not no melt in a puddle, but she couldn’t contain her smile, to her he was distant but now so close."

            show thalia o -bigBlush

            show ailon sad

            ailon "Phobion we talked before and you can’t scare my dates like this."

            show thalia satisfied smallBlush

            thalia "You said date… (she whispers softly)"

            phobion "You are right my loved Ailon, I was not chivalrous with lady, I’ll be of leave"

            show thalia confused -smallBlush

            show ailon o

            ailon "But get your suit checked out, I see some errors."

            phobion "My pleasure!"

            "Phobion walks away."

            hide phobion idle with dissolve

            show ailon at right, flip

            show thalia at left

            with dissolve

            "He than turns protagonist around, his face a mixture of worry and embarrassment."

            show ailon sad at right, reverseFlip

            ailon "I bet he said some weird things… he never really got over."

            show thalia o - bigBlush -bigBlush

            thalia "So he was an Ex…"

            ailon "I’m glad you got it, then… let’s walk around some more."

            show thalia satisfied

            thalia "Okay!"

            show thalia confused

            "When the initial shock wore off she looked to see if there was a trace of Phobion, she didn’t." 

            "Though outside she was happy as a butterfly she also thought it was very weird and she wanted to talk more to Phobion."

            jump choice3_END

        label choice3_B:

            $ phobianJealosly = True

            show thalia disgust

            thalia "Oh so you jealous of us?"

            phobion "I simply wanted to…."

            show thalia angry

            thalia "What to ruin a date? (She says a bit angry) I finally got him to enjoy a good time and you come between? I can make him happy enough thank you very much!"

            phobion "(Lifts up a hand as if to talk back) I… will let you threat thy path."

            hide phobion idle with dissolve

            "Phobion walks away, and soon Ailon comes around looking at Phobion."

            show ailon idle at right
            with dissolve

            ailon "Did he come talk you?"

            thalia "Yeah he was being mean… you shouldn’t hire your exs you know? (She laughs a bit)"

            show thalia thinking

            show ailon worry

            ailon "I… Well… Sorry about that… I’ll have to talk to him afterwards."

            show thalia sparkle
           
            show ailon o

            thalia "I wouldn’t worry too much (she grabs his hand and looks with sparkling eyes) I know I like you I just have to make sure you like me back~"

            show ailon blush
            
            show thalia convencida

            "Protagonist begging screaming internally, asking if she was to forwards, maybe to cringe?! Could he like her back."

            show ailon sweetsmile

            "Ailon gave in return smile and blushed cheeks."

            ailon "Well I won’t tell you yet…"

            show thalia happy

            show ailon smile 

            "There is a sweet air between the two"

            "Though Protagonist doesn’t see it, to chaotic her mind is there is a deep sadness forming in Ailons eyes, as if he is reading again a story he knows the end of it"

            "Both continue on their park adventure."
            
            jump choice3_END

        label choice3_END:
            jump choice2_END


# =========================part 3==================================
    label choice2_END:

    stop music fadeout 1.0
    
    scene bg parknigth

    play music "Contemplation.mp3"

    show thalia idle at left, smaller

    show ailon at right

    with dissolve

    if (phobianJealosly):
        jump part3b

    "They continued on to try other things, Mostly protagonist was adventuring around Foreverland, asking about the rides, and the different areas of the park."

    "The hours went by, the sun went down, and the lights came on, it gave a more mistic vibe to the whole place."

    "There were still many people around, but perhaps now most were tired from a day of playing around so it seemed more slow and calm."

    show thalia shinyeyes

    thalia "This place is so cool! It’s so different at night right?"

    show ailon smile

    "She was more stating than asking so Ailon kept quite, he didn’t seem tired but a bit distracted."

    thalia "Where did this come from anyway?"

    show ailon o

    ailon "(He was a bit confused) what you mean?"

    show thalia bigopen

    thalia "This park, its theme park, where did the ideia come from? Was it yours?… maybe your dad’s? This park has been here a while right?"

    ailon "It has yes, almost two hundred years the park has, but it wasn’t this big for a while."

    thalia "That’s so cool! So it does belong to your family who had the ideia?"

    show ailon side

    "Ailon seemed to shift a bit as if thinging, maybe a little to hard on the subject but then he spoke."

    ailon "My grandpa… he wanted to make a place for people he knew."

    show thalia o

    thalia "So he made a theme park? Not a hotel or maybe even a bar where he could have them around?"

    show ailon sad

    ailon "He… wanted to make them feel at home, that’s why he… made all these different areas."

    thalia "Oh! So there were all foreigners?"

    show ailon side

    ailon "Something like that…"

    show thalia happy

    thalia "Your grandad seems sweet then."

    show ailon sweetsmile

    ailon "(Playfully he said) so you were after my grandad not me? How scandalous!"

    show thalia convencida

    thalia "(Joking) Oh now I have been exposed! (She holds her hands to her chest)"

    ailon "Should have known you like them old!"

    show thalia happy

    thalia "They do have more experience, so maybe it’s for the best."

    show ailon smile

    ailon "Is that why you take a interest on me? Cause you think I’m old?"

    show thalia thinking smallBlush

    thalia "(She blushed a bit but said confidently) i don’t know you haven’t told me… but you do feel old…"

    show thalia nervous -smallBlush bigBlush

    show ailon surprise

    thalia "(She rapidly tries to save from calling this young man old) old in the good way I mean! Like that is confortable to be around you…"

    show thalia embarrased

    "Ailon seems a bit surprised but happy by the statement."

    menu part3choice:
        "Thalia blushes a bit while trying desperately to think how to change topics."

        "What do you like about me then?":
            jump part3choice_a
        "Do you believe in destiny? Like the woman said?" if meetIvania:
            jump part3choice_b
        "Who was that guy anyway? He said some strange things." if not meetIvania:
            jump part3choice_c
    
    label part3choice_a:

        "Ailon looked at her  for a moment, his mind seemed to drift a bit."

        show ailon idle

        show thalia o

        ailon "I guess… it would be your forwardness, i haven’t been one to begin things as of late, it’s refreshing."

        show ailon sad

        thalia "Everyone has bad times, you don’t need to feel so bad about."

        show thalia smile

        "Thalia put a hand in his shoulder as if to comfort him, she saw him as someone older but now he seemed smaller."

        ailon "I am humbled by your words but I don’t know if I can even be in this type of relationship you imagine right now…"

        "Even by his words he seemed to lean a bit forward, she saw there was this faint hope in his eyes."

        show ailon  verysurprise blush

        show thalia cutesmile at center

        "Thalia leaned a bit closer and gave him a kiss in the cheek "

        show thalia embarrased at left

        "He turned his eyes a bit shocked so she backed slightly embarrassed"

        show ailon sweet

        thalia "(She said nervously) I’m sorry… maybe i shouldn’t have done that…"

        ailon "(He was blushing and also a bit nervously) I… no you… its okay, I just wasn’t ready can you give me a minute?"

        thalia "(She was shocked) then… maybe I should go home…"

        show ailon sad blush

        ailon "No no, stay… i just need a minute to get my mind in order… here."

        show thalia o bigBlush

        "He approached her, pulled her hand and gave her a card."

        show ailon smile -blush

        ailon "You can use it to get something to eat around here if you are hungry… I’ll be back… just… don’t leave?"

        "He seemed genuinely confused in his feeling but his words seemed true"

        show thalia embarrased

        thalia "Okay… I’ll stay a bit."

        "He seemed relaxed and then nodded and walked away."

        hide ailon with dissolve

        "Thalia sat in a bench close by the put her hands in her hair embarrassed mumbling. "

        thalia "Oh no… now I messed it up… I shouldn’t have… but he looked so sad…"

        "Suddenly a figure of a man in a hood came by and said in a soft voice"

        jump harryNapped

    label part3choice_b:
        
        show thalia o

        thalia "You know… like what Ivania said."

        show ailon verymad

        ailon "(He seemed a little frustrated when he heard the name) she was trying to scare you like I said, it a bad habit she has."

        show thalia thinking

        thalia "But aren’t card readers supposed to tell truth on their cards."

        show ailon side

        ailon "But she exaggerated, it’s a park afterall, it has to bring some emotion."

        show thalia angry

        thalia "Then why are you so mixed up trying to dismiss what she said?"

        show ailon verymad

        show thalia bigopen

        ailon "Because I don’t wanna hurt you!"

        show thalia o

        show ailon worried

        "She was shocked, it the first time she saw him raise his voice, it wasn’t a scream per say, but as low as he talked it was loud."

        ailon "Oh I’m sorry… i didn’t mean to scream."

        show thalia convencida

        thalia "So you have a sensible side too… a bit childish too at that (she said smug)"

        show ailon surprise

        ailon "What?"

        show thalia thinking

        thalia "Every relationship is complicated, and sometime you hurt each other… you maybe older then me but I not naive like that."

        "Ailon looked surprised, he seems to expect something different, maybe rejection, but he got a response."

        thalia "So? You still wanna tell me the same?"

        show ailon sad

        show thalia angry

        ailon "It’s more complicated then that…"

        thalia "(She sighs) and they say woman are complicated…"

        show thalia at center

        show ailon surprise blush

        "She walks up to Ailon pulls him and gives him a fast kiss on the lips."

        "Inside she was so nervous she could be shaking, but she was also a bit angry, and wanted to show him her commitment."

        show thalia embarrased at left

        "Ailon looked shocked, then embarrassed, then the embarrassment came back to protagonist as well, She turned around and said."

        show ailon idle

        thalia "There… you either liked it… or didn’t."

        show ailon sad

        "There a strange moment of silence, but it felt longer for both."

        show thalia o bigBlush

        "Protagonist got even more embarrassed and she felt like she wanted to disappear she was getting ready to run off when Ailon grabbed her hand."

        ailon "I need a minute… and I think you do to… meet at the central plaza later… and have this, anything you want. Its is my treat."

        show thalia confused

        "He handed protagonist a small card, then walked away."

        hide ailon with dissolve

        "She was very shocked still, was that a good sing? A bad one?"

        "She stood there a bit giddy and did not see a man approach her."

        "He was wearing a hood and said in a soft voice."

        jump harryNapped
        
    label harryNapped:

        $ harryNapped = True
        
        show thalia at center

        show harry at shadowFilter,left, flip

        with dissolve
        
        "???" "Hey did he gave you a card?"

        show thalia confused -bigBlush at flip

        thalia "What…"

        "???" "Ailon, did he give you a card?"

        thalia "Yeah he did…"

        hide harry

        show harry at left, flip

        show thalia verysurprise

        "She stopped when she saw him pulling a gun, she thought about screaming there weren’t many people around but it was sure to draw attention."

        show thalia surprise

        "But she was so surprised it was like her body froze in fear."

        "???" "You scream you die… you run you die…you will get up, stand next to me and walk, then you live… nod if you understood."

        "Protagonist mind began racing with the very ideas he just warned her against, but if he was crazy enough to try and pull this in a park full of people, she might die."

        "As natural as she could she got up slowly and he came around the side putting the gun behind her and hiding between them."

        thalia "What…. What you want from me?"

        "???" "I want you to fucking live, now walk to that employee exit on the left."

        show thalia thinking at reverseFlip

        "She was confused but did as she was told."

        "Protagonist walked and he followed right up to the door."

        "???" "Use the card to open the door."

        show thalia angry

        "Still scared she pulled out the card, passed on the scanner beside the door, and to her surprise it worked."

        show harry smile

        "She heard a sight of relief, not from her but from the man he mumbled (it does work)."

        "He pushed her inside and closed the door behind them."
        
        jump part3end

    label part3choice_c:
        
        show thalia o
        
        ailon "Who do you mean?"

        show thalia o

        thalia "The one in the musketeer costume… Phobion I think seemed very well… you know."

        show ailon verymad

        ailon "He was just jealous and a bit confused I’m sure."

        show thalia confused

        thalia "Why do you keep him in the park?"

        show ailon surprise

        "Ailon seemed puzzled by the question, not as if he did know the answer but that he didn’t know how to tell her."

        show thalia o

        thalia" Maybe I should talk to him? Get him to understand that he can’t butt in like that."

        show ailon side

        ailon "You would stand up like that?"

        show thalia thinking

        thalia "Only because he didn’t seem to want to be mean about it… I mean he wasn’t mean, he was trying to tell me something."

        show ailon o

        ailon "Like what?"

        show thalia confused

        thalia "Just that you loved the people here… I think I was a bit confused too."

        show ailon idle

        "Ailon looked confused but then his face had a little more serious look, not in the threatening way but the determined look."

        show ailon sad

        ailon "Say Thalia do you still wanna talk to him?"

        thalia "Maybe I mean… he seemed to want to say things, it’s important to listen to people."

        ailon "Then would you listen to this?"

        show ailon idle blush at center

        "Ailon pulls her a bit closer, Thalia gets flustered and he leans in as if asking."

        show thalia bigopen bigBlush

        "Seing that, him asking for a kiss; Her heart was beating real fast and she agreed."

        show ailon sweet at right

        show thalia uwu

        "He kissed her for only o moment, leaving her dovey with love, he too was somewhat flustered."

        ailon "I… would you rather think of this instead… I should prepare something then."

        "He a bit clumsy searched his clothes and pulled a card."

        show ailon smile blush

        ailon "Have this to buy something if you are hungry, or show that to the employees, if ya need me, I’m gonna need a moment."

        hide ailon

        "He ran off before she could respond."

        "Her heart was beating so loud she could barely hear her own thoughts, but she could feel, besides the embarrassment and uneasiness."

        show thalia thinking

        "She took a long breath, looked around and went to talk to one of the employees."

        show thalia o -bigBlush

        thalia "Excuse me… I… I need to talk to Phobion."

        "I’m sorry Ma’am I don’t know what you mean."

        show thalia confused

        thalia "The musketeer Phobion… (she showed him the card) here can you take me to him."

        "The employee simply nodded in silence, and told her to follow."

        "She kept thinking about the kiss but this curiosity also was consuming her, so she was convicted to try her own path."

        "Both the employee and Thalia failed to notice a man following both, and he had been there a while."
        
        jump part3end
    
    label part3b:

        "Both Ailon and Thalia go on a lot of rides, they almost get to ride all of them before they stop to rest a while."

        "Thalia was feeling really happy but she didn’t know if Ailon was having the same amount of fun."

        "She saw him smile, talked to him, to her he did look handsome but it was making her somehow uncomfortable."

        "She also kept thinking back to that weird guy in the costume Phobion."

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

        show ailon side

        ailon "I’m just gonna talk to him not beat him."

        show thalia angry

        thalia "I know… but I’ll be bored without you here (she blinks her eyes as if making a charm)."

        show ailon smile

        ailon "Okay… then to make it up… this?"

        show thalia confused

        "He hands her a card."

        ailon "You should be able to get yourself anything you want."

        show thalia angry

        thalia "So you are buying me…?"

        show ailon o

        "Ailon seemed to be upset by her words, he meant to take the card but she backed a bit."

        show ailon sad

        "Inside her she began to dislike that off the ground side of him, that arrogance he knew better."

        "She wanted to be petty."

        show thalia thinking

        thalia "I didn’t say I wouldn’t take it."

        "Ailon seemed a bit sad by those words, she also began feeling a little bad by doing it."

        "He than turned his back and walked away."

        hide ailon with dissolve

        "Thalia was left to think and began talking to herself ."

        show thalia embarrased

        thalia "I like him… but now he just seemed weird, I don’t know if I like that."

        show harry at right ,shadowFilter

        "???" "Maybe you should find out what he is really doing."

        show thalia surprise

        "She hadn’t noticed but a man in a hoodie was juts next to her."

        "She jumped at his sudden appearance."

        show thalia o

        thalia "I’m sorry… do i know you?"

        "???" "No, but you don’t know Ailon either."

        "???" "He is hiding things from you."

        show thalia confused

        thalia "Like what?"

        "???" "That card does more than buy ya things, he just didn’t tell you."

        "The strange man gestures to an employee door."

        "Thalia feels really skeptical, and a bit scared so she does as she is told."

        "To her surprise after passing the card the door opens and inside her suspicion sets."

        show thalia surprise

        thalia "What now then?"

        "???" "Now we better go there before someone sees us. "

        "She goes in and the man follows closing the door behind."

        show thalia thinking

        hide harry
        show harry at right

        with dissolve

        harry "The name is Harry, lady… and you might need this."

        show thalia verysurprise

        "From under his hood he hands Thalia a gun."

        $ harryFriend = True

        jump part3end

    label phobionHurtB:

        show ailon sad

        ailon "It’s a long story… (he seemed sad)"

        show thalia o

        "She saw a slight pain in his eyes, she walked to a bench and gestured."

        show thalia idle

        thalia "Well luckily we got time."

        "He looked at the bench next to her and hesitantly sat down."

        thalia "I was… maybe a bit mean… I was upset; but you look sad, did you two had a long time together?"

        show ailon worry

        ailon "Yeah you could say that… but he wasn’t the only one."

        show thalia thinking

        "Thalia began to see that he seemed pained talking about it, perhaps way more the she expected."

        show thalia bigopen

        thalia "Maybe it’s still not the right moment to talk about it… but I’m glad you have shown it to me?"

        show ailon sad

        ailon "That I’m a mess."

        thalia "That you are human."

        show thalia  cutesmile

        show ailon surprise

        "(She laughs a bit akward)"

        "I think… honestly that you are very handsome… but it’s good to see that you are soft."

        show ailon idle

        "Ailon looked at her still a bit hurt but slightly more composed and looking up to her in a soft tender look, almost inviting."

        show ailon verysurprise blush

        show thalia at center

        "She leaned in and gave him a kiss."

        show thalia o bigBlush

        "I can be here for you… if you let me…"

        "Ailon didn’t say anything he seemed aloft and he blushed."

        show ailon idle

        "He stood up after a moment and handed her back a card."

        show ailon side

        ailon "Buy something to eat… I’ll be back in a bit I need to clear my head."

        show thalia embarrased

        thalia "Did I…"

        show ailon sad

        ailon "No no… it’s more me you can rest easy, I’ll be back if you still here."

        "She hesitate but took the card."

        hide ailon with dissolve

        "Before she could say anything he left."

        show thalia thinking

        "Thalia felt slightly awkward but relived she got to see a gentle and timid saúde of him, one that needed caring."

        show harry at shadowFilter, flip with dissolve

        "She didn’t notice a man in a hood getting close to her till he spoke."

        show thalia confused
        
        "???" "Do not scream… or you die."

        show thalia verysurprise

        "She looked and saw that the figure was holding a gun up to her, there were people around but in the quiet corner no one paid much attention."

        "Protagonist was shocked she couldn’t scream if she wanted to, so she just held the card firmly. "

        show thalia surprise

        "???" "You are going to get up, you won’t run or I’ll kill you… you are gonna come with me to that door, and you are gonna play it cool…. Nod if u understand."

        "Protagonist nooded, she wanted to run, she did want to scream, but what if he shot she thought."

        show thalia thinking

        "She did as he told her, got up, next to him, she felt the gun touch her back, as he hid it between them, and he whispered."

        "???" "Walk to the door and swipe the card."

        "She again did just like he said, her head was spinning and she felt her hands cold."

        "When she reached the door, there was a beep, the door opened, he pushed her inside and lock the door behind them, no one saw a thing."

        $ harryNapped = True

        jump part3end



    label part3end:

    if (harryNapped):
        jump loveRoute
    
    if (harryFriend):
        jump hateRoute
    
    jump pityRoute

    label loveRoute:

        "The hallway is obscure, clean, but very unsettling, there are few light lining the walls and the air is still and dry."

        "Some noises can be heard like machine working, water flowing in pipes. Only some talk could be heard in the far distance, probably from the park."

        "Thalia felt as the man behind her pressed the gun on her back and said."

        "???" "Now down the stairs"

        "She was scared enough to want to cry, but also to nervous to break down, as adrenaline also made her hyper aware, she managed to walk."

        "They were in a catwalk that oversaw the hallways, they went down and surprisingly only the sound of machinery could be heard."

        "He made her walk up to a junction. An automated maintenance car drove by the junction, it was so silent she couldn’t hear unto it passed right In front of her."

        thalia "(She mustered up courage to speak) What do you want from me…?"

        "???" "Like I said for you to live, now tell me where the other people are."

        thalia "What? Who?" 

        "???" "The people that monster keeps down here, it’s the only place he can hide that many people; Take me to them!"

        thalia "Mister (she said scared) I don’t even know who you are honestly… please don’t hurt me…"

        "She started to think he was crazy, he pushed her so she was facing him and said "

        "The name is Harry… Harry Kepleer and you lady?"

        "He also took his hood off, to her surprise it was an older man, she expected a mean looking thug, but not a grandpa, he looked well over sixty."

        thalia "It’s Thalia… (she was confused and manages to answer only because her expectations were thrown off)."

        harry "Look, I don’t wanna kill you okay, just that bastard… so I need you to tell me where his people are."

        thalia "His… who?"

        harry "Ailon’s, the people he has kidnapped and imprisoned."

        thalia "What?!"

        "Thalia was hit with a mixture of shock and fear, could Ailon be some sort of psychopath, she thought."

        "She could only think about his smile and his face, how friendly he was, could it be she was wrong about him."

        "That can’t be… he is a sweet person… and a bit sad but he couldn’t be kidnapping… people…"

        harry   "You don’t know… (he looked disappointed and tired) but he gave you that card… he must trust you."

        thalia 'He just gave me to buy something… i thought it was a gift card to the park.'

        harry "It indeed is, but it’s one that belongs to him so it must grant access to theses levels and much more around the park."

        thalia "Why would he give it to me then?"

        harry "You didn’t know it could be used like that maybe…"

        "He seemed confused, Thalia saw maybe an opportunity to run away but she didn’t know where to."

        "That’s when from one of the door came one of the parks full suits, it was a man dressed like a pirate."

        "Pirate man" "Hey mateys… you cannot be in this boat."

        "Thalia saw as an opportunity to scream for help."

        thalia "Please help he has a gun!"

        "The man looked at her angry, he pointed the gun at the full suit mascot."

        "Pirate man" "If this is a munity you will walk the plank mat…."

        "He didn’t finish the sentence and the loud bang of a gun shot hit the mascot straight in the chest."

        "Thalia watched horrified, but to her surprise the man did not fall, and no blood formed in the whole."

        "The pirate man simply lunged forward without saying anything, as Harry fired three more shots each hitting a part."

        "Thalia tried to run but she hit a maintenance cart that was waiting right behind her to pass, she tripped and fell."

        "The pirate man also fell in the ground, she then felt the man grab her arm."

        thalia "Please… please don’t kill me ( this time she cried a bit)."

        harry "Look for yourself he ain’t human!"

        "He dragged her closer to the body, she was too nervous and scared to fight back so he showed her."

        "The suit was half open on the back, and inside the suit there were machine pieces fused with flesh, it barely spewd blood, it was grotesque to look so she looked away"

        harry "I don’t know if they are alive… but they sure ain’t living."

        "Pirate man" "Thalia matey… (the voice said a mix of robotic cracking) the captain will be here…"
        
        harry "Shit!"

        "Harry dragged Thalia away"

        "As she was being dragged she saw the suit still try to move in her direction but right there was nothing she could do."

        "The man dragged her only up to the next corner, then forced her to walk the hallways."

        "Thalia cried, she kept thinking what was going on, people fused with machines, was that really all Ailon?"

        "Harry was lost, he wandered the hall, many door had weird symbols?, he tried opening some of them, but they were mostly empty except for some strange surgical equipment he refused to touch, but took some pictures."

        "They finally came across a stranger door it had a bridge simbol."

        "Harry was frustrated and he stopped and looked at the door for a moment."

        harry "Better this than anything else. Open it."
        
        "Thalia walked to the door and swiped the card."

        "The door opened revealing a larger room, in much the same style of the hallways, but in its center up on a pedestal rested what looked like an obsidian dagger."

        "Maybe blacked from time, it was a crude piece, just like something out of the pre-historic times."

        harry "What the fuck…"

        "Stay here…"

        "Harry walked up to the pedestal, it had a glass dome on top of it."

        "He pointed the gun a took a shot, the glass exploded and Thalia put her hands in her ears, she thought about running."

        "Just then two hands around her shoulder calmly, she looked and saw Ailon."

        "It was mixed feeling relief but also scared, who was this man next to me now she thought, and he had somewhat scary expression."

        "Harry then turned around."

        harry "You fucker!"

        "He pointed the gun at Ailon"

        harry "I saw the messed up shit here you did, you pick up people and turn them into monsters!"

        ailon "I do no such thing… (Ailon sounded angry, yet bored)."
        
        "I saw them don’t deny it, I’m going to expose you and your sick family"

        ailon "I don’t have a family it’s all me Harry…"

        harry "How do you… you know what fuck you!"

        "Harry pulls the trigger, Thalia watched horrified as a bullet wound opened straight into Ailons head and he fell in the ground"

        "She screamed horrified and confused but she was even more confused when he stood up"

        "Ailon simply got up, the bullet wound expelled out the metal pellet."

        ailon "Happy?"
        
        harry "You are a monster"

        "Harry shot him two more time but Ailon Barr even fell into the ground"

        "Thalia fell on her knees scared, her mind running surprise after surprise she felt like she would faint."

        "Harry picked up the knife and tried to charge at Ailon "

        "Ailon for the first time seem genuinely angry as he also charged the man"

        ailon "Let go of that knife!"

        "Not only was a man in his prime against an old man, but also seemed like a warrior against a child, as Ailon simply dogged the thrust, flipped the man’s arm and trip him down."

        "The sound of the man hitting the ground was heavy and likely broke a bone or two."

        "Some people in the full suits came in and grabbed the man."

        "And Thalia from full exhaustion also fainted."

        "When she woke up it was on a mattress laid out in the main plaza of the park."

        "She thought she was dreaming, there was no people around but sitting by a bench was Ailon quite and looking sad."

        "He still held the black knife in his hands. Thalia sat up on the mattress, her head a mess full of thoughts and fears."
        
        thalia "Who are you?"

        "Ailon looked at her, and she could almost feel a weight on him, like he was dragging himself to every action she could fear him but also pity him"

        "He got up leaving the knife where it was, he sat just a bit away from her and said"

        ailon "I’m Ailon… and I can’t die…"

        "Thalia was confused and bewildered, but if she saw what she saw, him getting shot and shrugging it off like some super hero she couldn’t lie to herself "

        "She struggled to find out what to say, but could still see Ailons sadness"
        
        thalia "Tell me more… what was all that I saw down there?"

        ailon "I can’t even think where to start…"

        thalia "Maybe tell me… what is going on… who was that man who are you really?"

        "Ailon looked bitter and sad but he seemed trufull in his words."

        ailon "My name is Ailon…"

        ailon "I have been cursed Thalia… to live forever, I have since a very long time"

        ailon "That man… Harry… his grandfather was involved in trying to pin me on vengeance because years ago his wife left his grandfather and he, belived my family were criminals."

        ailon "Only it was me…"

        thalia "Did you… kill…"

        ailon "No no… I’ll think about what to do with him later, i don’t really wanna hurt an old man like him."

        thalia "I see… that’s reasonable."

        "What… were those things… I saw down there"

        "There was hesitation in her voice to ask, like she feared the answer it self"

        ailon "Do you see the knife? The black one"

        "Thalia saw from afar the rustic dagger still on the bench." 

        thalia "Yeah…"

        ailon "It was used to kill me a long time ago… I don't know why but i survived, or came back…"

        "Since then I haven’t aged and can’t be killed"

        "Also anyone that is stabbed with it… if their love is selfish they’ll be immortal too…"

        thalia "I… don’t get it."

        ailon "Me either, but I have been told it is such… should I be stabbed and their love be selfless I will die… "

        "And their granted immortality is unfortunately not good either…"

        thalia "Is it bad?"
        
        ailon "Unfortunately yes… the world is unfair…"

        "I don’t know if you knew but the human brain can only retain so much information."

        "After about 120 years you brain literally can’t hold anymore information."

        
        "Thalia looked confused but paid attention to his words"

        ailon "So people that became immortal like that eventually can’t hold anymore information"

        "They go insane Thalia"

        "There have been hundreds of men and women I loved… that said they loved me… but just…"

        "A few tears rolled on his cheeks."

        ailon "They went insane! I’m fine but they love their minds…"

        ailon "So those suits… is how I keep them alive and safe…"

        ailon "The areas in the park work to much the same… to feel like they are in their own time, makes them docile"

        thalia "But aren’t they insane?! What if they hurt someone."

        ailon "That’s what the suit is for… their body… I fused it with the suit, and their brains are lobotomised so they can be docile."

        "Thalia was horrified, they were people after all."
        
        thalia "How could you…? To them? Didn’t you love them?"

        ailon "I DID!"

        ailon "But if I let them lose?! What then?"

        ailon "They can’t die! They either be Aimesley ruining around hurting people or kept in lab!"

        ailon "Here they have what little… what little comfort I can give!!!"

        "To Thalia what he said was still insane, but it could be true, he seemed genuine."

        "Both in his sadness and his logic."

        "Looking at it if they truly were insane, as cruel as his method was he was keeping them from being used by other people."

        "Ailon seemed to shake, tears still flowed, they were genuine and to her that made it clear he at least was trying to be good."

        thalia "You… what do you want then?"

        ailon "What I want."

        ailon  "I want to die Thalia! I want this to end."

        ailon "I have seen cities raised in the name of conquest and then torn down and fade in the dust."

        ailon "I have watched men go from wearing pelts to operating machines to reach space."

        ailon "I have loved and I have hated!"

        ailon "I have been a king and a beggar!"

        ailon "Done. It. ALL!"

        ailon "All but have an end to this!"

        thalia "Do you want it to end?"

        ailon "By every fiber of me yes… the people I loved are gone, walking corpser for all I know, people hunting me for things they can’t understand."

        ailon "I seem to have this allure… that makes me wanna claw my own face off but it would just grow back."

        ailon "I wonder if you humans like this sort of madness."

        "There was frustration in his tone."

        "But Thalia listened carefully to his ramble."

        "She got up and walked closer to him."

        thalia "I can say I still feel some atraction… and I can’t tell if you are bad… or just hurt, like anyone would for all this time."

        thalia "I have asked you to open your heart for me many times and you did… just now you are telling me truth."

        thalia "Why?"

        ailon "I… wish I knew."
    
        "Thalia looked at this broken men with kindness, she could feel the weight he carried on his shoulders."
        
        "And deep inside she wanted to help him."

        "To her what little time they had showed a person hurt by time but of a cruel kindness, a cruelty forced by impossible choices."

        "She didn’t want to think much anymore about all of that."

        "She hugged Ailon."

        thalia "I get it… at least part of it, I can’t hate you… even with all of this…"

        ailon "You are insane… "

        thalia "Maybe you just passed that to me"

        
        "She got up and walked to bench and picked up the black knife."

        "It really did look like something that came from the Stone Age." 

        ailon "What are you…?"

        thalia "You said that if someone loves you… it will kill you right? Does it hurt to try?"

        "He looked shocked and stood up."


        ailon "But Thalia you don’t love me…"

        thalia "Love has many faces you dummy…"

        thalia "I really liked our time… I liked your company… I liked you."

        thalia "But your suffering… and your eyes I can see your pain."

        ailon "It won’t work Thalia… plus I don’t wanna make you do this to me for u to…"

        thalia "I’ll just have a few nightmares and it will be over (she was putting a brave face but she too couldn’t believe she was thinking about killing him)."

        ailon "You would do this… for me? Why?"

        thalia "Because it is what you want right? For your story to end…"

        thalia "It does make me sad… really really sad but it is your wish right?"

        thalia "I think I can... Do something for you."

        ailon "But I haven’t given you anything… you will Be leaving with nothing out of this."
        
        thalia "You make it sound like I need something"

        thalia "I don’t, you told me your wish."

        thalia "Truthfully..." 

        thalia "And I want to help you."

        "Ailon looked baffled and then a laugh so loud she couldn’t believe it came from him."

        ailon "I have never seen…. That…. Something I haven’t seen in so many years of life, a girl so lovesick as you!"

        thalia "Hey!!"

        "From all the tense and sadness they both laughed in a rare moment of joy."

        "And Thalia knew she felt a little tingly feeling."

        "She grasped that moment imprinting in her memory and charged with the knife in hand."

        "She didn’t quite feel as the knife hit Ailon, she closed her eyes before hitting him."

        "She heard his voice sweet say."

        ailon "Ya got me…"

        "She felt to the ground."

        "As she looked Ailon was no where in sight."

        "Only a small pile of ash"

        thalia "I hope that made you free… I wish."

        "I just wished we could have had more dates…"

        "Such a shame you were such a cutie…"

        "She cried a whole bunch."

        "Time moved on and so did she."

        "Thalia discovered that all the costumes had turned to dust to, seems that with the curse gone all the immortals were too."

        "Harry made news trying to spill the beans on Ailon, but he was gone with no trace, and so was half the park."

        "Even though the park had lost half its people and Ailon, it seems he had everything in place for it to work without him."

        "Thalia went back to her life, but she carried on her memory those memories with Ailon, she held on to that feeling of kindness despite all the sadness."

        "She went to the park still every now and then, and went on her life, she looked back at it kindly and moved on."

        "SELFLESS LOVE ENDING"

        jump end

    label hateRoute:
        jump end

    label pityRoute:

        "The woman took Thalia only a little distance away and pointed out to an employee only entrance."

        "Employee" "Just go through there, down the stairs and to the repair room."

        thalia "Right… the repair room."

        "The woman then gave Thalia a polite nod and walked away."

        "Thalia felt confused, she looked at the door, then to the card in her hands."

        "There was a small console beside the door so she swiped the card and the door unlocked."

        "Hesitant she walked in."

        "It was was a catwalk overlooking a maintenance hallway, the place was filled with pipes and wiring, it was an unsettling."

        "Thalia heard the door close, then open again for a moment, she looked but there was no one, only some soda crate near by."

        thalia "I don’t really think I should be here but oh well…"

        "She shrugged and walked down the stairs the ground floor of the hallway had rails where automated carts delivered goods around the park."

        "She couldn’t hear any noise from the park itself, only some mechanical machine sounds and liquids flowing in the pipes."

        thalia "Right… repair room… but where…"

        "Thalia was uneasy the place was by itself weird, she chose to go left."

        "A cart rushed by her she had to sidestep quickly so it didn’t hit her."

        "She walked to another intersection, she thought to herself she would get lost here before she found the repair zone."

        "Fortunately for her as she looked around the intersection on one side standing in the middle of the hallway was Phobion."

        "Thalia approached carefully."

        thalia "Phobion… you okay?"

        "Phobion turned and it seemed he stood right in front of a cart that darted forward the moment he stepped away, she did too."

        "But back in the intersection a voice complained and the sound of a crash."

        "Thalia backed away towards Phobion and a man made around the corner."

        phobion "Fair lady from earlier the day… who is the farthest gentleman from us."

        thalia "I don’t… know, who are you mister?"

        "The man simply laughed and pulled out a gun."

        "???" "You monsters get down on your knees."

        "Thalia was first shocked her whole body froze in place, at the sight."

        Phobion "This is not a toy to wave around, brave gentleman, put down at once."

        "The man shot the gun in the roof, the loud bang rippled across the halls."

        "In was enough to make Thalia let a scream of panic."

        "So the man pointed the gun at her, until Phobion stepped between both."

        phobion "I warn only once my great gentleman, or I shall Draw my blade against thee."

        "???" "Oh yeah? Fucking creep!"

        "The man shot at Phobion’s leg, Thalia looked horrified as Phobion came to one knee and the man said."

        "???" "Try it now."

        "Thalia kneeled down to try and help but she was surprised to see Phobion get up as if nothing happened."

        "A small blood clot forming on his leg, still Phobion pulled out his rapier, it was this blunt prop that was something you could buy in any store."

        "The man looked surprised under the hood, but it was hard to tell."

        "???" "Try it… and this time I kill you boy."

        Phobion "I fear no failure."

        "And again to Thalia's horror Phobion charged the man."

        "The gun roared fire and lead in response, at least three or four shots, all which hit Phobion."

        "He did not stop, he charged the man no fear, and plunged the prop into the man’s torso."

        "It was a metal still, blunt, yet with enough force, it could hurt someone and that it did."

        "Only when Thalia saw the sword impale the man did she manage to close her eyes in fear."

        "There was the sound of something falling, likely the man’s body, then a few steps followed by a similar yet heavier sound."

        "When she opened her eyes, she saw in the further distance the man impaled, dead, she avoided but saw Phobion close."

        thalia "Oh my… oh my god… oh shit…"

        "She hesitated but walked to him and turned his body around."

        "There were some bullets wounds in his chest, yet very little blood."

        thalia "I need to find help I…"

        "Phobion grabbed her hand as she made the move to stand up."

        phobion "You do not have to, o shall live through this danger."

        thalia "No… you… you were shot! You need help!"

        phobion "Fair lady I will not perish here, but do help me sit, I need but moment of rest."

        "Hesitant Thalia helped him sit, leaning against the wall, she tried not to look at the dead man in the distance."

        thalia "At least… let me take a look at it maybe I can improvise some bandages."

        phobion "There is no need…"

        "She ignored him and she grabbed the suit carefully, pulling clothing."

        "She froze when what she saw was flesh fused with machine parts, there was only a small entry wound of the bullet, no blood was flowing like it had almost healed already."

        "Yet it was a horrific sigh, his flesh was cut where cables and metallic joints met flesh and muscle."

        "Thalia jumped back and screamed horrified."

        "Phobion grabbed the torn clothing and covered the exposed inside." 

        phobion  "Fear not, I am fine."

        thalia "Who… who did this to you?!"

        phobion "Beloved Ailon has seen it so."

        thalia "What… why!? "

        "Thalia felt her heart drop, could sweet Ailon hurt people like this, could she be next?"

        phobion "He did so to help myself."

        thalia  "How is that helping?!"

        "There were sounds of small pellets hitting the ground, she looked and saw the bullets had been expelled from his body."

        phobion "My life is one to be forever lady, shots will not kill me! Neither will blades or time!"
 
        "Her mind began racing many questions, but mostly she was happy he seemed okay."

        thalia "But… why are you in this state."

        phobion "Oh unfortunately that is something beyond my knowledge hoho! Only Ailon can say."

        thalia "So you don’t know why?"

        phobion  "Only that I have been here a long time!"

        thalia "And you can’t leave?"

        phobion "I choose to stay to for Ailon, he be lonely if no one was near."

        "Thalia remember how sad and lonely he looked, now she wanted to talk to him and ask personally."

        thalia "Then I need to find him!"

        phobion "I think i know he must should be near the plaza I can take you the way."

        thalia "Are you sure you can… walk?"

        "He got up in a strange fashion but seemed fine."

        phobion "Nothing will ever stop courage and honor!"

        "Thalia laughed"

        "She tried to look ta the dead man but Phobion put himself between them."

        phobion "Do not think of it, I shall solve this evildoers fate, you have done no wrong."

        "That made her feel bad but she also didn’t want to look at it, she hesitated but began walking the other way."

        phobion "I also… believe I have been most blunt I my manners… may I ask this fair lady name?"

        thalia "It’s Thalia."

        phobion "It good to know… I should tell the others too."

        thalia "There are other people like you? In the park?"

        phobion "That is matter better asked to Ailon not?"

        thalia "Maybe… okay I will."

        "Phobion took her around the tunnels, they must have walked for some good minutes before they climbed some stairs and were back in the park."

        "Phobion however still had his costume damaged so he stayed inside and said."

        phobion "He should be here, good luck lady Thalia… and please be kind to him… I remember him a kind soul."

        thalia "I… will try."

        "Phobion went back and Thalia looked around for Ailon."

        "She saw him sitting down alone, he seemed confused and sad."

        "She felt embarrassed about the kiss but mustered courage to walk to him."

        thalia "Hey Ailon…"

        "He seemed startled by her voice and looked at her confused."

        thalia "We should talk…"

        ailon "I… (he was a bit red) thought you were back there still… how did you find me?"

        thalia "Phobion said you would be here…"

        ailon "You… talked to Phobion?"

        "He seemed to be slightly more serious that it was a bit scary he then said."

        ailon "And what did you talk about?"

        thalia "He told me some things… about himself and you… but I thought I should ask myself."

        ailon "Okay just… keep here and don’t move… I mean it."

        "Ailon looked very serious it was almost scary."

        "He then stood up and talked to some of the staff, the blocked part of the plaza and told people it was under maintenance."

        "The park was already closing and there were only people far away now, and they were alone."

        ailon "What exactly happened?"

        "Ailon was serious and there was also some anger in his voice."

        "Thalia was surprised to see him that way but after what happened she was more confused."

        thalia "I went after Phobion… to ask him about you… and well a man followed me, when I found Phobion he pulled a gun on us."

        "Ailons posture changed as he focused his attention."

        ailon "Did he hurt you?"

        thalia " No… Phobion I think he… he might have killed him…"

        ailon "Killed him?!"

        thalia  "He was trying to shot at him."

        ailon "Where is he now?"

        thalia "I don’t really know, down the maintenance tunnels, Phobion didn’t let me look a second time."

        "Ailon looked like he was about to get up but Thalia grabbed his arm."

        thalia "Phobion also got shot… but he lived… I saw underneath his clothes too."

        "Ailons eyes twitched, a mix of shame, surprise and fear, Thalia didn’t know which was stronger so she continued." 

        thalia "He said he was immortal… that I should ask you… Ailon what is going on?"

        "Ailon took a deep breath and his eyes almost swelled with tears."

        ailon "He did not lie… he is… and so am I."

        "Thalia was surprised to say the least, first she did not believe but then she saw a man get shot and get up like nothing."

        thalia "How?!"

        ailon "I was cursed, a very long time ago, to live forever…"

        thalia "How long…"

        ailon "Longer than I would like."

        thalia "What you mean by that?"

        ailon "Thalia I have been around since man lived in caves!"

        "Thalia got scared for a moment at his outburst as he continued to spill his fury"

        ailon "And I can’t stand anymore."

        "I have seen more then I would like to see."

        "You wanted to know what Phobion had to tell you?!"

        "I cursed him too, so has mostly every poor soul in this park!"

        "They were once people I loved but are now shells of themselves."

        "And I can’t take it anymore!"
        
        "He fell to his knees crying and Thalia rushed to him sitting down in the ground with him."

        thalia "It’s okay… I don’t think I understand all of it but I see you…"

        ailon "No you don’t…"

        "He pushed her."

        ailon "His body I did that!"

        ailon "I had too, they all go mad with their immortality! It was the only way to keep him safe."

        ailon "And I had to do it…"

        ailon "So many times..."

        ailon "You see this sad man?!"

        ailon "I’m an immortal being who trapped the people he loved in metal sarcophagus like broken toys I’m a monster!"

        thalia "You are suffering!"

        ailon "Yes Thalia I am!"

        ailon "Because this fucking life…. This fucking mind or body keeps me alive unlike all the people I love."

        ailon "Thalia Is there no way to end it? (She hesitated to ask)."

        ailon "The only way to do it is if someone who loves me selflessly used a knife to kill me."

        "Thalia was puzzled, yet everything about this day was weird, she imagined it was part of the curse so she yellow."

        thalia "Bring the knife here then!"

        ailon "What?"

        thalia "I like you… despite what you said I still do… let me try!"

        ailon "Are you insane?!"

        thalia "To try and help someone?"

        ailon "by stabbing me?"

        thalia "You don’t die do you?"

        ailon "It still hurts like a bitch."

        "There was strange pause and an awkward laugh between the two."

        thalia "Bring it here… I have seen a lot today.. I want to help."

        ailon "You are unbelievable…"

        "Thalia felt a bit angry at his comment but also proud."

        "Yet felt this whole thing was almost unreal."

        "Ailon got up his expression seemed very sad."

        "Thalia reached out her hand but she neither reached nor could say anything."

        "A few moments passed and she was all alone in the plaza."

        "Her head filled with thoughts of the day."

        "She did still, despite all think kindly of Ailon, she wanted to help him, if that somehow had to end with his end maybe it was for the best."

        "But she also did not want that, she wanted to spend more time with him, to know him better to understand his view."

        "Her thoughts cut short when he came back carrying a very old knife."

        "It looked like something you would see in a museum, it seemed fashioned from a dark rock with a leather grip."

        ailon "I have it here…"

        "She could see in his face doubt, shame but maybe a hope this could give him what he wanted."

        thalia "So that knife… made you and the others… imortals?"

        ailon "Yes…"

        thalia "And you make people imortal by being stabbed? Who even came up with that?"

        ailon "If you know, do tell me… I have some complaint to them."

        "Again Thalia looked awkward at the object and at him not knowing exactly what to say."

        "Ailon took a step and handed her the knife taking again a step back."

        ailon "Do it fast… just in the stomach… it don’t hurt as bad and easier to strike"

        thalia "You seem to know."

        ailon "Not the first time I tried it…"

        "Thalia was hesitant, would it work? She couldn’t know, was he insane? Maybe but it seems it was what he wanted."

        "She looked at him, he close his eyes in a serene way and braced."

        "Thalia thought she wanted to spend time with him and this could be the end of it."

        "So she decided on a new course of action."

        "Ailon heard a striking sound and a welp not his own, opening his eyes Thalia had stabbed herself."

        ailon "No!"

        "He rushed to her cradling her head."

        "She gave him a sad look as desperation spread across his face, but then her eyes had a kind manner."

        thalia "Now I’ll be immortal too… and you won’t be alone."

        ailon "No Thalia it had to me to do it! You are just gonna die like this!"

        thalia "Oh… (she felt guilty about it as her mind felt cloudy) I didn’t know… guess I’m silly."

        ailon "No no… I didn’t want this… you gonna make me go trough this again…"

        thalia "What are you talking about… it’s my fault really… but I would like… a hospital."

        ailon "You … you… I don’t want to lose you either… not like this… I …"

        "If he finished Thalia didn’t hear it."

        "She felt her body get cold but then a sharp pain on her neck."

        "Her conscience seemed to fade, like melting deep in a river."

        "Then she felt hot and burning sensation and a jolt of pain made her sit down and scream."

        thalia "Oh shit! Ouch!"

        "She looked as Ailon sat just across from her his head down, the knife in his hands and bloodied."

        "She touched her stomach and the wound was gone but she felt her clothes a bit soggy with blood, her neck too."

        thalia "Did you?"

        ailon "I killed you… before you bled out yourself… now you are…"

        thalia "Immortal?"

        ailon  "I’m sorry…."

        "He began to cry almost child like and Thalia again hugged him saying."

        thalia "Ailon you saved me from my own self stupidity, I’m fine."

        ailon "No you are not! Don’t you get it."

        "He stood up."

        "You cannot live forever you will lose your mind! I have condemned you to live like a shell till the end of time! All because I was too weak…"

        "To let you die…"

        thalia "You are not weak! You are kind!"

        ailon "Kindness has nothing to do with this! It’s fact."

        "The human brain can’t retain information after certain time, in 100 years you won’t be yourself anymore."

        thalia "I won’t! I’ll be here still."

        ailon "I… I’m done… then do just that."

        "His whole silhouette seemed to grow tired and weary, completely devasted."

        "It lasted only a moment but in the next."

        "He beamed a smile, almost to perfect to be honest but it did fool Thalia that she thought his saddens turned to relief."

        ailon "Lets make the best then, of the years to come!"

        "Thalias heart was relieved and she smiled kindly at him as she made the decision to stay by his side."

        thalia "I’m glad I got through your thick skull."

        "The man that Phobion killed went unnoticed, and not even the police came looking for him, apparently it was deemed a missing person and there was nothing liking him to the park."

        "Whatever he came here to do, he did it in secret and it was his undoing."

        "Thalia lived along with Ailon for many years helping in the park, going on dates."

        "She did try using the knife but it never worked, but they were happy nonetheless."

        "Until about 150 years later Thalia seemingly lost interest in living things, she began with animals, Ailon did not notice… but the change happened and it only grew."



        
    label end:
    
    return