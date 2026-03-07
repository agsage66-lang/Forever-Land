# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define thalia = Character("Thalia", color = "#f27d83")

define friend = Character("Thalia's Friend", color = "#846FB7")

define ailon = Character("Ailon", color = "#A0B3BA")

define ivania = Character("Ivania", color = "#316374")

define phobion = Character("Phobion", color = "#316374")

define harry = Character("Harry", color = "#E5AE6E")

define anon = Character("???", color = "#ffffff")

define employee = Character("Employee", color = "#ffffff")


#flags

default phobianJealosly = False

default meetIvania = False

default harryNapped = False

default harryFriend = False

#image control

image white = "#ffffffff"

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
        attribute terrified1:
            "thalia_terrified1"
        attribute terrified2:
            "thalia_terrified2"
        attribute terrified3:
            "thalia_terrified3"

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

    group extras:
        attribute noeffect default:
            null
        attribute blush :
            "ailon_blush"
        attribute shadow :
            "ailon_shadow"

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

    thalia "I was so great! Like, amazing, he is very quiet, but those eyes~ dreamy."

    show thalia uwu

    thalia "He was very quiet, but truly I couldn’t get enough for just one date, especially his eyes. I wanna look at them again."

    show friend blush

    friend "Sounds like he has you hooked…"

    show thalia convencida

    thalia "On the other way around, I have him hooked!"

    show friend worry

    friend "It’s not what it sounds like…"

    show thalia thinking smallBlush
    thalia "Oh shut up… I played it cool"

    "Outside a well-dressed man with a calm, serene expression, walks towards the store. Thalia quickly hides their face and whispers."

    show thalia bigopen
    
    thalia "OMG, it’s him! He is coming here!"

    show friend surprise

    friend "Did you invite him?"

    thalia "No… do you think it’s like fate?! We meet again, like boom! Sparks!"

    friend "Calm down, you have to play it cool. will you to talk to him?"

    show thalia thinking bigBlush

    thalia "Maybe…"

    show friend tired

    "The man walks in the store, his calm demeanor and presence seem to fill the room with ease, slowly he makes his way to the cashier."

    ailon "One coffee, black, large, with cream."

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
    
    ailon "Well I come here almost every day, it’s a nice place."

    show thalia satisfied

    thalia "Oh really that’s so nice… than I’m glad I chose to come here."

    show thalia nervous

    menu choice1 :
        "There a moment of this weird silence as Thalia thinks about what to say."
        "Ask why this store":
            jump choice1_A
        "Ask if he is free later":
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

        ailon "But it was fortunate to meet you again today… I was thinking if you wanted to go somewhere again… with me?"

        show thalia verysurprise

        thalia "Oh… oh… oh!!!!"

        show thalia verysurprise bigBlush
        show ailon sweet

        thalia "Yes I’d like that very much!"
        
        jump choice1_END
    
    label choice1_B:

        show thalia nervous

        thalia "After this, are you doing anything? If you are not, I’d love for a… second date maybe…"

        show ailon surprise

        "He looks puzzled and surprised, a smile comes around his features lighting up the room."

        show ailon smile

        ailon "I’m glad you asked, I would be willing, yes."

        show thalia happy

        thalia "Are you free today maybe? I wasn’t doing much, so I could go out this afternoon even!"

        show ailon sweetsmile

        ailon"Well… I could yes."

        show thalia idle

        thalia"Since I chose last time do you wanna pick a place?"

        jump choice1_END

    label choice1_END:

    show ailon smile    
        
    ailon "There is an amusement park here, Foreverlands, I happen to, know some one there… and they can get us in no problem."

    show thalia happy -bigBlush

    thalia "That sounds so cool, who knew you were that well connected."

    show ailon o

    ailon "Then when?"

    show thalia idle

    thalia "Oh right right… maybe two hours in the main gate? I don’t wanna leave my friend just like this."

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

    "Beyond the painted walls and decorated fences one can see the rollercoasters tracks, fabricated mountains and one of the largest ferries wheel in the country."

    "There are various sounds of laughter and chatter that mix around the smell of fresh cooked popcorn and baked sweets that can make one flutter with anticipation."

    "Thalia is waiting beneath a small shade in the sidewalk, because even with the nice weather, staying out in the open is asking for a sun burn."

    "She can barely contain the smile across her face, even after getting scolded by her friend, she more than wished her luck on this date."

    "She was in the middle of talking to herself as if practicing flirts."
    
    show thalia sparkle

    thalia "So are you bringing me to the park because you wanted to do funny business with me?!"

    show thalia thinking bigBlush

    thalia "no no… that's to forward and too weird."

    show ailon idle at right, with dissolve

    "Ailon comes into her field of view from the crowd close to the gate."

    show thalia verysurprise

    "Thalia tries to hide a bit of the embarrassment from the attempted flirt as he approaches."
    
    show thalia o

    show ailon smile

    ailon "I hope you didn't wait long in this sun… You looked like you were talking to someone. Did I interrupt?"

    show thalia nervous -bigBlush

    thalia "No… I… was… well… just talking a bit to myself, you know? Making some mental notes… I remember things better when I say them outloud!"

    show thalia verysurprise

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

    "When they walk in, she can feel a cooler breeze, inside is full of color and people; most are just chatting from one ride to the next, others are looking at the stores."

    "This part of the park looks like a small village. Foreverlands is mostly this medieval western fantasy theme; even the staff are either dressed as knights or peasants."

    "Thalia had been there before but not enough to remember most of it."

    show thalia o -smallBlush

    thalia "Oh my god, it does feel so fresh in here. How did you know?"

    show ailon o

    ailon "We keep the fans well positioned to help the airflow."

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

    thalia "You say that like it's any less amazing!!"

    show thalia shinyeyes

    show ailon smile

    thalia "Do you get to go on the rides whenever you want? Do you have an infinite supply of popcorn? Can you close the park if you wanted to?"

    show thalia embarrased

    thalia "Oh… am I talking to much…"

    "Ailon tried and failed to hold back his laughter, but he managed to be composed enough to say."

    show ailon sweetsmile

    ailon "No, but you are very loud."

    "Thalia looked around to see some people confused by all the noise and some curious; it was not every day you see the owner of the park."

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

        "There are less rides in this part, but many more stores and game stands that are supposed to more closely resemble various old settlements" 

        "Many thematic areas are skillful placed to each be their own separate area, there are western, eastern, egipician, Nordic and even some pre historic theme"

        show thalia o

        "Thalia's stops to look around an intersection of these areas"

        show thalia happy

        show ailon smile

        thalia "This is so cool, it’s like miniature museums in here."

        thalia "Do you have any favorites?"

        ailon "Well…not really but this area as a whole is one I take a personal attachment to."

        show thalia o

        thalia "Oh? Are you really into history?"

        show ailon side

        ailon "You could say that yes, all of those places once were the worlds to various civilizations and different cultures."

        show ailon smile

        ailon "They each had even their own way of seeing our world never mind the language, most are unique in their respective ways."

        "Ailon stops as he sees Thalia is starring at him."
        
        show ailon worry blush

        ailon "Sorry did I say something too boring?"

        show thalia satisfied

        thalia "It was the most I’ve seen you speak, I was very interested!"

        thalia "You almost like a teacher… by the way, I've never asked but how old are you? To be all like a 'grandpa on history'."

        show ailon smile -blush

        ailon "Can’t say, I stopped counting."

        show thalia pouts

        thalia "But birthday’s are so fun!"

        show ailon sweet

        show thalia happy

        "They both laugh at this."

        "Something caught Thalia's attention, in a tribal tent there was this comical, lady in a costume, with cards and lots of feathers."

        show thalia o

        thalia "Is that a card reader?"

        show ailon smile

        ailon "Yes, her name was Ivania."

        show thalia happy

        thalia "I thought tribal readers did it like with bones and smoke, not cards."

        show ailon surprise

        thalia "I’m gonna give it a try anyway, come on!"

        show ailon worry
 
        "Ailon seems to try and grab her hand, but Thalia slips and goes straight inside the tent."

        scene bg tent

        stop music fadeout 1.0

        show thalia satisfied at smaller, left
        with dissolve

        play music "wind_chimes_loop_3.ogg"

        "There is a faint smell of oil, and a small pillow to kneel on, she sits and looks at the woman."

        show ivania idle at right with dissolve

        "The woman named Ivania seems just a bit older than her, she is in a full costume, making her features a bit stiff, and her whole body slightly bigger."

        "Thalia wondered if it was stuffy in there, or why wasn’t it easier to just dress up in a full suit."

        ivania "Welcome wonderer!" 

        show thalia shinyeyes
        
        "Her mouth moved slightly as she spoke, it was very cool how she could move like that, but perhaps just a bit stiff."

        thalia "So cool you can move your mouth!"

        ivania "I can also tell you about your future, do you want to unmask your destiny?"

        thalia "I do!"

        show thalia o

        ivania "Ivania pulled out from the side five cards, but they weren’t the size of normal playing cards, they were slightly bigger than a hand."

        ivania "She then laid them in front of Thalia, a bit of smoke rose from the corners."

        "Ailon walked up to the corner of the tent but stood outside, Thalia was too focused to notice his presence. He seemed uneasy."

        ivania "I will now begin with a sight of the past."

        "She took the first card and put it in a pot, with one finger she seemed to draw inside."

        show thalia at lightFilter , left

        show ivania at lightFilter

        show cards time at top, smaller with dissolve

        ivania "Time itself follows you, closer than you think."

        "She puts down the card with a sketch of a clock over a feminine figure in red tinture"

        ivania "Now for the sight of your present"

        "She does the same thing with the second card"

        "She puts down a big heart and many arrows"

        show cards heart

        ivania "Love is pulling in either direction, it will either be your pity or kindness that will take you forward."

        "She picks up the third card."

        "After drawing she says before putting it down."

        ivania "You will see the end of your current world."

        show cards bridge

        "The card shows a broken bridge overlooking a view."

        thalia "Is that bad?"

        "Ivania picks both of the last cards, she quickly draws on both, squeezing them together, she says in a whisper."

        ivania "It will depend in where will the dagger land."

        "She shows almost identical cards, on one is a woman one is man, and a black dagger is embedded in both."

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

        ailon "She is playing to make you believe in disaster, it's always does this to make a shock, she does that all the time!"

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

        thalia "Oh, so it won’t be so fun if you already know… but do you still want to?"

        ailon "They are made to be fun; I don’t mind going again if that’s what you want."

        show thalia uwu

        "The smile feels Thalia with some butterflies, his smile is so composed, that you could take a picture from any angle and it would look great, she thinks that at least."

        show thalia verysurprise

        show ailon idle -blush

        thalia "Say, since you own this place… could we skip ahead?"

        show ailon sweetsmile

        ailon "I did not take for a rule breaker miss Thalia…"

        show thalia sparkle
 
        thalia "You got me I was a bad girl."

        ailon "I guess a bit of rules bending can’t hurt."

        show thalia convencida

        "Ailon takes Thalia by the hand up towards the front of the line"

        "Her heart pounds like a child on Christmas Eve, she suggested it herself before but having him do it made her happy"

        show thalia idle

        show ailon o

        "He talked real quick to one of the employees, they let both walk in, some people looked at them weird but perhaps they just had a fast pass."

        show thalia satisfied

        show ailon sweetsmile

        "The ride was fast, it was supposed to be like eletricity traveling across lightbulbs."

        "When they both made it out and Thalia said."

        thalia "It was almost a light show, everything was so fast!"

        show ailon smile

        ailon "So it was fun?"

        show thalia shinyeyes

        thalia "Real real fun! What next? You wanna choose?"

        ailon "I have a feeling you will know best"

        thalia "Than this way!"

        hide thalia 
        
        hide ailon

        with dissolve

        "They both spend some time from ride to ride."

        "Eventually Ailon asks for a moment to go to the toilet, so Thalia waits."

        hide ailon

        "While she waits one of the characters, a figure that resembles a Musketier approaches and says."

        show thalia o at smaller, left with dissolve

        "Is this fine lady on her own?"

        show thalia happy

        show phobion idle at right

        with dissolve

        thalia "It seems not any more sir."

        "She can she it is another full suit, she really hopes it's not hot in there"

        "It’s also very sophisticated, it looked cartoonish enough to be abstract but can also move it's mouth it a robotic manner"

        show thalia idle

        phobion "I was Knight Phobion, My fine lady!"

        show thalia o

        phobion "Say have you walk this parts with he?"

        show thalia confused

        thalia "With he?"

        phobion "The love of those in the park, most of us were here for him, I saw thou from afar."

        show thalia verysurprise

        thalia "Oh you mean Ailon like… oh my god he is your boss right?"

        phobion "He was many to us, part of us, now he seeks you."

        show thalia bigopen

        thalia "You mean you think he likes me?"

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

            thalia "You said date…"

            phobion "You are right my loved Ailon, I was not chivalrous with lady, I’ll be off leave"

            show thalia confused -smallBlush

            show ailon o

            ailon "But get your suit checked out, I see some errors."

            phobion "My pleasure!"

            "Phobion walks away."

            hide phobion idle with dissolve

            show ailon at right, flip

            show thalia at left

            with dissolve

            "He than turns Thalia around, his face a mixture of worry and embarrassment."

            show ailon sad at right, reverseFlip

            ailon "I bet he said some weird things… he never really got over."

            show thalia o - bigBlush -bigBlush

            thalia "So he was an Ex…"

            ailon "I’m glad you got it, then… let’s walk around some more."

            show thalia satisfied

            thalia "Okay!"

            show thalia confused

            "When the initial shock wore off she looked to see if there was a trace of Phobion, there wasn't." 

            "Though outside she was happy as a butterfly she also thought it was very weird and she wanted to talk more to Phobion."

            jump choice3_END

        label choice3_B:

            $ phobianJealosly = True

            show thalia disgust

            thalia "Oh so you jealous of us?"

            phobion "I simply wanted to…."

            show thalia angry

            thalia "What to ruin a date? I finally got him to enjoy a good time and you come between? I can make him happy enough thank you very much!"

            phobion "I… will let you threat thy path."

            hide phobion idle with dissolve

            "Phobion walks away, and soon Ailon comes around looking at Phobion."

            show ailon idle at right
            with dissolve

            ailon "Did he come talk you?"

            thalia "Yeah he was being mean… you shouldn’t hire your exs you know?"

            show thalia thinking

            show ailon worry

            ailon "I… Well… Sorry about that… I’ll have to talk to him afterwards."

            show thalia sparkle
           
            show ailon o

            thalia "I wouldn’t worry too much. I know I like you I just have to make sure you like me back~"

            show ailon blush
            
            show thalia convencida

            "Thalia begging screaming internally, asking if she was to forwards, maybe to cringe?! Could he like her back."

            show ailon sweetsmile

            "Ailon gave in return a smile and blushed cheeks."

            ailon "Well I won’t tell you yet…"

            show thalia happy

            show ailon smile 

            "There is a sweet air between the two"

            "Though Thalia doesn’t see it, to chaotic her mind is there is a deep sadness forming in Ailons eyes, as if he is reading again a story he knows the end of it"

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

    "They continued on to try other things. Dragging Ailon along Thalia was adventuring around Foreverland, asking about the rides, and the different areas of the park."

    "The hours went by, the sun went down, and the lights came on, Making the place even more mystical."

    "There were still many people around, but perhaps now most were tired from a day of playing around so it seemed more slow and calm."

    show thalia shinyeyes

    thalia "This place is so cool! It’s so different at night right?"

    show ailon smile

    "She was more stating than asking so Ailon kept quite, he didn’t seem tired but a bit distracted."

    thalia "Where did this come from anyway?"

    show ailon o

    ailon "What you mean?"

    show thalia bigopen

    thalia "This park, it's theme park, where did the ideia come from? Was it yours?… Maybe your dad’s? This park has been here a while right?"

    ailon "It has yes, almost two hundred years the park has, but it wasn’t this big for a while."

    thalia "That’s so cool! So it does belong to your family! Who had the ideia?"

    show ailon side

    "Ailon seemed to shift a bit as if thinking, maybe a little to hard on the subject, but then he spoke."

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

    ailon "So you were after my grandad, not me? How scandalous!"

    show thalia convencida

    thalia "Oh now I have been exposed!"

    ailon "Should have known you like them old!"

    show thalia happy

    thalia "They do have more experience, so maybe it’s for the best."

    show ailon smile

    ailon "Is that why you take a interest on me? Cause you think I’m old?"

    show thalia thinking smallBlush

    thalia "I don’t know! You haven’t told me… But you do feel kinda old…"

    show thalia nervous -smallBlush bigBlush

    show ailon surprise

    thalia "Old in a good way, I mean! Like, in a way, that is comfortable to be around you…"

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

        ailon "I guess… it would be your forwardness, I haven’t been one to begin things as of late, it’s refreshing."

        show ailon sad

        thalia "Everyone has bad times, you don’t need to feel so down about."

        show thalia happy

        "Thalia put a hand in his shoulder as if to comfort him, she saw him as someone older but now he seemed smaller."

        ailon "I am humbled by your words but I don’t know if I can even be in this type of relationship you imagine right now…"

        "Even by his words he seemed to lean a bit forward, she saw there was this faint hope in his eyes."

        show ailon  verysurprise blush

        show thalia cutesmile at center

        "Thalia leaned a bit closer and gave him a kiss in the cheek "

        show thalia embarrased at left

        "He turned his eyes a bit shocked so she backed slightly embarrassed"

        show ailon sweet

        thalia "I’m sorry… maybe i shouldn’t have done that…"

        ailon "I… no you… its okay, I just wasn’t ready can you give me a minute?"

        thalia "Then… maybe I should go home…"

        show ailon sad blush

        ailon "No no, stay… I just need a minute to get my mind in order… here."

        show thalia o bigBlush

        "He approached her, pulled her hand and gave her a card."

        show ailon smile -blush

        ailon "You can use it to get something to eat around here if you are hungry… I’ll be back… just… don’t leave?"

        "He seemed genuinely confused in his feeling and his words seemed true"

        show thalia embarrased

        thalia "Okay… I’ll stay a bit."

        "He seemed relaxed, then nodded and walked away."

        hide ailon with dissolve

        "Thalia sat in a bench close by then put her hands in her hair embarrassed and mumbling. "

        thalia "Oh no… now I messed it up… I shouldn’t have… but he looked so sad…"

        "Suddenly a figure of a man in a hood came by and said in a soft voice"

        jump harryNapped

    label part3choice_b:
        
        show thalia o

        thalia "You know… like what Ivania said."

        show ailon verymad

        ailon "She was trying to scare you like I said, it a bad habit she has."

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

        show ailon worry

        "She was shocked, it was the first time she saw him raise his voice, it wasn’t a scream per say, but as low as he talked it was loud."

        ailon "Oh I’m sorry… i didn’t mean to scream."

        show thalia convencida

        thalia "So you have a sensible side too… a bit childish too at that."

        show ailon surprise

        ailon "What?"

        show thalia thinking

        thalia "Every relationship is complicated, and sometimes you hurt each other… You may be older than me but I'm not naive like that."

        "Ailon looked surprised, he seemed to expect something different, maybe rejection, but he got a response."

        thalia "So? You still wanna tell me the same?"

        show ailon sad

        show thalia angry

        ailon "It’s more complicated than that…"

        thalia "And they say woman are complicated…"

        show thalia at center

        show ailon surprise blush

        "She walks up to Ailon and pulls him close, and gives him a quick kiss on the lips."

        "Inside she was so nervous she could be shaking, but also a bit angry, and wanted to show him her commitment."

        show thalia embarrased at left

        "Ailon looked shocked, then flustered, then the embarrassment came back to Thalia as well. She turned around and said:"

        thalia "There… you either liked it… or didn’t."

        show ailon sad

        "There's a strange moment of silence, but it felt longer for both."

        show thalia o bigBlush

        "Thalia got even more embarrassed, feeling like she wanted to disappear. She was getting ready to run off when Ailon grabbed her hand."

        ailon "I need a minute… and I think you do too… meet me at central plaza later… and have this, anything you want. Its is my treat."

        show thalia confused

        "He handed Thalia a small card, then walked away."

        hide ailon with dissolve

        "She was still very shocked, was that a good sign? A bad one?"

        "She stood there a bit giddy and didn't notice a man approach her."

        "He was wearing a hood and said in a soft voice."

        jump harryNapped
        
    label harryNapped:

        $ harryNapped = True
        
        play music "hbs.mp3"

        show thalia at center

        show harry at shadowFilter,left, flip

        with dissolve
        
        anon "Hey did he give you a card?"

        show thalia confused -bigBlush at flip

        thalia "What…"

        anon "Ailon, did he give you a card?"

        thalia "Yeah he did…"

        hide harry

        show harry at left, flip

        "She stopped when she saw him pulling a gun, she thought about screaming, there weren’t many people around but it was sure to draw attention."

        show thalia terrified1

        "But she was so surprised it was like her body froze in fear."

        anon "You scream you die… you run, you die… you will get up, stand next to me and walk, then you live… nod if you understood."

        "Thalia's mind began racing with the very ideas he just warned her against, but if he was crazy enough to try and pull this in a park full of people, she might die."

        "As natural as she could, got up slowly and he came around the side putting the gun behind her, hiding it between them."

        show thalia surprise

        thalia "What…. What you want from me?"

        anon "I want you to fucking live, now walk to that employee exit on the left."

        show thalia thinking at reverseFlip

        "She was confused but did as she was told."

        "Thalia walked and he followed right up to the door."

        anon "Use the card to open the door."

        show thalia angry

        "Still scared she pulled out the card, passed on the scanner beside the door, and to her surprise it worked."

        show harry smile

        "She heard a sight of relief, not from her but from the man he mumbled."

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

        thalia "Only because he didn’t seem to want to be mean about it… he wasn’t mean, he was trying to tell me something."

        show ailon o

        ailon "Like what?"

        show thalia confused

        thalia "Just that you loved the people here… I think, I was a bit confused too."

        show ailon idle

        "Ailon looked confused but then his face had a little more serious look, not in the threatening way but the determined look."

        show ailon sad

        ailon "Say Thalia do you still wanna talk to him?"

        thalia "Maybe I mean… he seemed to want to say things, it’s important to listen to people."

        ailon "Then would you listen to this?"

        show ailon sad blush at center

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

        thalia "The musketeer Phobion… Here can you take me to him."

        "The employee simply nodded in silence, and told her to follow."

        "She kept thinking about the kiss but this curiosity also was consuming her, so she was convicted to try her own path."

        "Both the employee and Thalia failed to notice a man following both, and he had been there a while."
        
        jump part3end
    
    label part3b:

        "Both Ailon and Thalia go on a lot of rides, they almost went on all of them before they stoped to rest a while."

        "Thalia was feeling really happy but she didn’t know if Ailon was having the same amount of fun."

        "She saw him smile, talked to him, to her he did look handsome but it was making her somehow uncomfortable."

        "She also kept thinking back to that weird guy in the costume, Phobion."

        show thalia confused

        thalia  "Ailon, why would you keep an Ex you had, working here?"

        show ailon surprise

        ailon "What you mean by it?"

        show thalia thinking

        thalia "Phobion he was trying to talk to me, to I think… make me not like you, why do keep him employed? Isn’t it uncomfortable?"

        show ailon sad

        ailon "Should I fire him because of a relationship? he can be good at his job…"
        
        show thalia pouts

        show ailon surprise

        thalia "Not good if he bothers our date!"

        "She is feeling something other than bother but she can’t quite place the feeling, so she looks at him to see what he says."

        show ailon side

        ailon "You know… you are right… I should go give him a piece of mind."

        show thalia confused

        thalia "Now?"

        ailon "Well in case he comes bother us again."

        menu phobionHurt:
            "She was upset he was stepping away but happy he seemed to mind the date enough, and that somehow made her feel relieved."

            "Tell him if he bothers us again I’ll kick his butt":
                jump phobionHurtA
            "Why was he that hurt?":
                jump phobionHurtB

    label phobionHurtA:

        show ailon side

        ailon "I’m just gonna talk to him not beat him."

        show thalia angry

        thalia "I know… but I’ll be bored without you here."

        show ailon smile

        ailon "Okay… then to make it up… this?"

        show thalia confused

        "He hands her a card."

        ailon "You should be able to get yourself anything you want."

        show thalia angry

        thalia "So you are buying me…?"

        show ailon o

        "Ailon seemed to be upset by her words, he meant to take the card back but she snatched it."

        show ailon sad

        "Inside her, she began to dislike that aloft side of him, that arrogance he knew better."

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

        anon "Maybe you should find out what he is really doing."

        show thalia surprise

        "She hadn’t noticed but a man in a hoodie was juts next to her."

        "She jumped at his sudden appearance."

        show thalia o

        thalia "I’m sorry… do i know you?"

        anon "No, but you don’t know Ailon either."

        anon "He is hiding things from you."

        show thalia confused

        thalia "Like what?"

        anon "That card does more than buy ya things, he just didn’t tell you."

        "The strange man gestures to an employee door."

        "Thalia feels really skeptical, and a bit scared so she does as she is told."

        "To her surprise after passing the card the door opens and inside her mind, suspicion sets in."

        show thalia surprise

        thalia "What now then?"

        anon "Now we better go there before someone sees us. "

        "She goes in and the man follows closing the door behind."

        show thalia thinking

        hide harry
        show harry at right

        with dissolve

        harry "The name is Harry, lady… and you might need this."

        show thalia verysurprise

        "From under his hoodie he hands Thalia a gun."

        $ harryFriend = True

        jump part3end

    label phobionHurtB:

        show ailon sad

        ailon "It’s a long story…"

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

        thalia "Maybe it’s still not the right moment to talk about it… but I’m glad you have told me"

        show ailon sad

        ailon "That I’m a mess."

        thalia "That you are human."

        show thalia  cutesmile

        show ailon surprise

        "She laughs a bit akward"

        thalia "I think… honestly that you are very handsome… but it’s good to see that you are soft."

        show ailon idle

        "Ailon looked at her still a bit hurt but slightly more composed and looking up to her in a soft tender look, almost inviting."

        show ailon verysurprise blush

        show thalia at center

        "She leaned in and gave him a kiss."

        show thalia o bigBlush

        thalia "I can be here for you… if you let me…"

        "Ailon didn’t say anything he seemed aloft and he blushed."

        show ailon idle

        "He stood up after a moment and handed her back a card."

        show ailon side

        ailon "Buy something to eat… I’ll be back in a bit I need to clear my head."

        show thalia embarrased -bigBlush

        thalia "Did I…"

        show ailon sad

        ailon "No no… it’s more me, you can rest easy, I’ll be back if you still here."

        "She hesitate but took the card."

        hide ailon with dissolve

        "Before she could say anything he left."

        show thalia thinking

        "Thalia felt slightly awkward but relived she got to see a gentle and timid side of him, one that needed caring."

        show harry at shadowFilter, flip with dissolve

        play music "hbs.mp3"

        "She didn’t notice a man in a hood getting close to her till he spoke."

        show thalia confused
        
        anon "Do not scream… or you die."

        show thalia terrified1

        "She looked and saw that the figure was holding a gun up to her, there were people around but in the quiet corner no one paid much attention."

        "Thalia was shocked she couldn’t scream if she wanted to, so she just held the card firmly. "

        show thalia surprise

        anon "You are going to get up, you won’t run or I’ll kill you… you are gonna come with me to that door, and you are gonna play it cool…. Nod if u understand."

        "Thalia nooded, she wanted to run, she did want to scream, but what if he shot she thought."

        show thalia thinking

        "She did as he told her, got up, next to him, she felt the gun touch her back, as he hid it between them, and he whispered."

        anon "Walk to the door and swipe the card."

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

        scene bg hallway

        show thalia thinking at smaller, center

        show harry at left , flip
        
        "The hallway is obscure, clean, but very unsettling. There are few light lining the walls and the air is still and dry."

        "Some noises can be heard like machine working, water flowing in pipes. Only some talk could be heard in the far distance, probably from the park."

        "Thalia felt as the man behind her pressed the gun on her back and said."

        anon "Now down the stairs"

        "She was scared enough to want to cry, but also too nervous to break down, as adrenaline also made her hyper aware, she managed to walk."

        "They were in a catwalk that oversaw the hallways, they went down and surprisingly only the sound of machinery could be heard."

        "He made her walk up to a junction. An automated maintenance car drove by the junction, it was so silent she couldn’t hear unto it passed right In front of her."

        show thalia disgust

        thalia "What do you want from me…?"

        anon "Like I said for you to live, now tell me where the other people are."

        thalia "What? Who?" 

        anon "The people that monster keeps down here, it’s the only place he can hide that many people; Take me to them!"

        show thalia angry

        thalia "Mister, I don’t even know who you are honestly… please don’t hurt me…"

        "She started to think he was crazy, he pushed her so she was facing him and said "

        harry "The name is Harry… Harry Kepleer and you lady?"

        "He also took his hood off, to her surprise it was an older man, she expected a mean looking thug, but not a grandpa, he looked well over sixty."

        show thalia surprise

        thalia "It’s Thalia…"

        show thalia o

        harry "Look, I don’t wanna kill you okay, just that bastard… so I need you to tell me where his people are."

        thalia "His… who?"

        harry "Ailon’s, the people he has kidnapped and imprisoned."

        show thalia verysurprise

        thalia "What?!"

        "Thalia was hit with a mixture of shock and fear, could Ailon be some sort of psychopath, she thought."

        "She could only think about his smile and his face, how friendly he was, could it be she was wrong about him."

        "That can’t be… he is a sweet person… and a bit sad but he couldn’t be kidnapping… people…"

        harry   "You don’t know… but he gave you that card… he must trust you."

        show thalia o

        thalia 'He just gave me to buy something… i thought it was a gift card to the park.'

        harry "It indeed is, but it’s one that belongs to him so it must grant access to theses levels and much more around the park."

        thalia "Why would he give it to me then?"

        harry "You didn’t know it could be used like that maybe…"

        "He seemed confused, Thalia saw maybe an opportunity to run away but she didn’t know where to."

        show pirate idle at right

        "That’s when from one of the door came one of the parks full suits, it was a man dressed like a pirate."

        anon "Hey mateys… you cannot be in this boat."

        "Thalia saw as an opportunity to scream for help."

        show thalia shout

        thalia "Please help he has a gun!"

        hide thalia

        show thalia verysurprise at left, smaller

        show harry at center

        with dissolve

        "The man looked at her angry, he pointed the gun at the full suit mascot."

        anon "If this is a munity you will walk the plank mat…."
        
        show white 

        play sound "gunshot.mp3"

        show black with fade

        "He didn’t finish the sentence and the loud bang of a gun shot hit the mascot straight in the chest."

        "Thalia watched horrified, but to her surprise the man did not fall, and no blood formed in the whole."

        "The pirate man simply lunged forward without saying anything, as Harry fired three more shots each hitting a part."

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade        

        "Thalia tried to run but she hit a maintenance cart that was waiting right behind her to pass, she tripped and fell."

        hide white
        
        hide black with dissolve

        "The pirate man also fell in the ground, she then felt the man grab her arm."

        show thalia terrified2

        thalia "Please… please don’t kill me."

        show harry smile

        harry "Look for yourself! He ain’t human!"

        "He dragged her closer to the body, she was too nervous and scared to fight back so he showed her."

        show harry at left

        show thalia verysurprise at center

        with dissolve

        "The suit was half open on the back, and inside the suit there were machine pieces fused with flesh, it barely spewd blood, it was grotesque to behold so she looked away."

        show thalia terrified1

        thalia "What... What are they?!"

        harry "I don’t know if they are alive… but they sure ain’t living."

        anon "Thalia matey… The captain will be here…"

        show thalia o

        show harry -smile
        
        harry "Shit!"

        hide pirate

        show thalia verysurprise

        with dissolve

        "Harry dragged Thalia away"

        "As she was being dragged she saw the suit still try to move in her direction but there was nothing she could do."

        "The man dragged her only up to the next corner, then forced her to walk the hallways."

        show thalia terrified2

        "Thalia cried, she kept thinking what was going on, people fused with machines, was that really all Ailon?"

        "Harry was lost, he wandered the hall, many doors had weird symbols, he tried opening some of them, but they were mostly empty except for some strange surgical equipment he refused to touch, but took some pictures."

        "They finally came across a strange door with a bridge symbol."

        "Harry was frustrated and he stopped and looked at the door for a moment."

        harry "Better this than anything else. Open it."
        
        "Thalia walked to the door and swiped the card."

        scene bg knife

        with dissolve

        "The door opened revealing a larger room, in much the same style of the hallways, but in its center up on a pedestal rested what looked like an obsidian dagger."

        "Maybe blacked from time, it was a crude piece, just like something out of the pre-historic times."

        show harry at right

        show thalia surprise at left, smaller
        with dissolve

        harry "Stay here…"

        show thalia o

        "Harry walked up to the pedestal, it had a glass dome on top of it."

        show thalia verysurprise

        show white 

        play sound "gunshot.mp3"

        hide white with fade

        "He pointed the gun a took a shot, the glass exploded and Thalia put her hands in her ears, she thought about running."

        "Just then two hands rested around her shoulder calmly, she looked and saw Ailon."
        
        show thalia surprise at flip, center

        show ailon verymad at left, flip

        with dissolve

        "It was mixed feeling relief but also scared, who was this man next to me now she thought, and he had somewhat scary expression."

        "Harry then turned around."

        harry "You fucker!"

        "He pointed the gun at Ailon"

        show ailon at center

        show thalia terrified1 at left

        with dissolve

        harry "I saw the messed up shit you do here, pick up people and turn them into monsters!"

        show ailon side

        ailon "I do no such thing…"
        
        harry "I saw them don’t deny it, I’m going to expose you and your sick family."

        show ailon sad

        ailon "I don’t have a family it’s all me Harry…"

        harry "How do you… you know what! Fuck you!"

        show white 

        play sound "gunshot.mp3"

        show black with fade

        "Harry pulls the trigger, Thalia watched horrified as a bullet wound opened straight into Ailon's head and he fell to the ground."

        "She screamed horrified and confused but she was even more baffled when he stood up."

        "Ailon simply shrugged, the bullet wound expelled the lead pellet."

        ailon "Happy?"
        
        harry "You are a monster"

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade 

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade 

        "Harry shot him two more time but Ailon simply took the shots without a sound."

        "Thalia fell on her knees terrified, her mind fuming with this scene, feeling like she would faint."

        "Harry picked up the knife and tried to charge at Ailon "

        "Ailon for the first time seem genuinely angry as he also charged the man."

        ailon "Let go of that knife!"

        "Not only was Ailon in his prime against an old Harry, but also seemed like a warrior against a child, as Ailon simply dogged the thrust, flipped the man’s arm and triped him down."

        "The sound of the man hitting the ground was heavy and likely broke a bone or two."

        "Thalia, overwhelmed with everything, fainted from exhaustion."

        scene bg parknigth

        show thalia thinking at smaller, left

        with dissolve

        play music "Lavender.ogg"

        "When she woke up it was on a mattress laid out in the main plaza of the park."

        show thalia verysurprise

        "She thought she was dreaming, there was no people around, but sitting by a bench was Ailon a somber expression stamped all across his features."

        "He still held the black knife in his hands. Thalia sat up on the mattress, her head was a mess full of thoughts and fears."

        show ailon worry at right

        show thalia angry
        
        with dissolve 

        thalia "Who are you?"

        "Ailon looked at her, and she could almost feel a weight on him, like he was dragging himself to every action she could fear him but also pity him."

        "He got up leaving the knife where it was, he sat just a bit away from her and said."

        ailon "I’m Ailon… And I can’t die…"

        "Thalia was confused and bewildered, but if she saw what she saw, him getting shot and shrugging it off like some super hero she couldn’t lie to herself."

        "She struggled to find out what to say, but could still see Ailons sadness."
        
        thalia "Tell me more… what was all that I saw down there?"

        show ailon sad

        ailon "I can’t even think where to start…"

        show thalia o

        thalia "Maybe tell me… what is going on… who was that man who are you really?"

        "Ailon looked bitter and sad but he seemed truthfull in his words."

        ailon "My name is Ailon…"

        show ailon side

        ailon "I have been cursed Thalia… To live forever... I have since a very long time."

        show ailon worry

        ailon "That man… Harry… his grandfather was trying to pin on me, vengeance because years ago his wife left his grandfather, and he, belived my family were criminals."

        ailon "Only it was me…"

        show thalia verysurprise

        thalia "Did you… kill…"

        show ailon sad

        ailon "No no… I’ll think about what to do with him later, i don’t really wanna hurt an old man like him."

        show thalia thinking

        thalia "I see… that’s reasonable."

        show thalia confused

        thalia "What… were those things… I saw down there?"

        "There was hesitation in her voice to ask, like she feared the answer itself."

        show ailon worry

        ailon "Do you see the knife? The black one."

        "Thalia saw from afar the rustic dagger still on the bench." 

        thalia "Yeah…"

        show ailon side

        ailon "It was used to kill me a long time ago… I don't know why but i survived, or came back…"

        ailon "Since then I haven’t aged and can’t be killed"

        show ailon sad

        ailon "Also anyone that is stabbed with it… if their love is selfish they’ll be immortal too…"

        thalia "I… don’t get it."

        ailon "Me Neither, But I have been told it is such… If I am stabbed by this, and the person bears a true selfless love, it will end the curse and I will die."

        ailon "And their granted immortality is unfortunately not good either…"

        thalia "Is it bad?"

        show ailon worry
        
        ailon "Unfortunately yes… the world is unfair…"

        ailon "I don’t know if you knew but the human brain can only retain so much information."

        ailon "After about 120 years you brain literally can’t hold anymore information."

        "Thalia looked confused but paid attention to his words"

        show ailon sad

        show thalia o

        ailon "So people that became immortal like that eventually can’t hold anymore information"

        ailon "They go insane Thalia."

        ailon "There have been hundreds of men and women I loved… that said they loved me… but just…"

        "A few tears rolled on his cheeks."

        show ailon worry

        ailon "They went insane! I’m fine but they lose their minds…"

        ailon "So those suits… is how I keep them alive and safe…"

        ailon "The areas in the park work to much the same… To feel like they are in their own time, makes them docile"

        show ailon side

        show thalia angry

        thalia "But aren’t they insane?! What if they hurt someone."

        ailon "That’s what the suit is for… their body… I fused it with the suit, and their brains are lobotomised so they can be docile."

        "Thalia was horrified, they were people after all."

        show thalia disgust
        
        thalia "How could you…? To them? Didn’t you love them?"

        show thalia surprise
        
        show ailon verymad

        ailon "I DID!"

        show ailon worry

        ailon "But if I let them lose?! What then?"

        ailon "They can’t die! They either be aimesly ruining around hurting people or kept in lab!"

        ailon "Here they have what little… what little comfort I can give!"

        show ailon sad

        show thalia o

        "To Thalia what he said was still insane, but it could be true, he seemed genuine."

        "Both in his sadness and his logic."

        "Looking at it if they truly were insane, as cruel as his method was he was keeping them from being used by other people."

        "Ailon seemed to shake, tears still flowed, they were truthfull and to her that made it clear that he at least was trying to be good."

        thalia "You… what do you want then?"

        show ailon verymad

        ailon "What I want."

        ailon  "I want to die Thalia! I want this to end."

        ailon "I have seen cities raised in the name of conquest and then torn down and fade in the dust."

        ailon "I have watched men go from wearing pelts to operating machines to reach space."

        ailon "I have loved and I have hated!"

        ailon "I have been a king and a beggar!"

        ailon "Done. It. ALL!"

        show ailon sad

        ailon "All but have an end to this!"

        show thalia angry

        thalia "Do you want it to end?"

        show ailon worry

        ailon "By every fiber of me yes… the people I loved are gone, walking corpses for all I know, people hunting me for things they can’t understand."

        ailon "I seem to have this allure… that makes me wanna claw my own face off but it would just grow back."

        show ailon sad

        ailon "I wonder if you humans like this sort of madness."

        "There was frustration in his tone."

        "But Thalia listened carefully to his ramble."

        "She got up and walked closer to him."

        show thalia confused

        show ailon worry

        thalia "I can say I still feel some atraction… and I can’t tell if you are bad… or just hurt, like anyone would for all this time."

        thalia "I have asked you to open your heart for me many times and you did… just now you are telling me the truth."

        thalia "Why?"

        show ailon sad

        ailon "I… wish I knew."
    
        "Thalia looked at this broken men with kindness, she could feel the weight he carried on his shoulders."
        
        "And deep inside she wanted to help him."

        "To her what little time they had showed a person hurt by time but of a cruel kindness, a cruelty forced by impossible choices."

        "She didn’t want to think much anymore about all of that."

        hide thalia

        show thalia happy at center, smaller

        show ailon surprise

        with dissolve

        "She hugged Ailon."

        show thalia o

        thalia "I get it… at least part of it, I can’t hate you… even with all of this…"

        ailon "You are insane… "

        thalia "Maybe you just passed that to me."
        
        hide thalia

        show thalia thinking at left, flip, smaller

        with dissolve
        
        "She got up and walked to bench and picked up the black knife."

        "It really did look like something that came from the Stone Age." 

        ailon "What are you…?"

        show thalia o at reverseFlip

        with dissolve

        thalia "You said that if someone loves you… it will kill you right? Does it hurt to try?"

        "He looked shocked and stood up."

        show ailon sad

        ailon "But Thalia you don’t love me…"

        show thalia happy

        thalia "Love has many faces you dummy…"

        show thalia embarrased

        thalia "I really liked our time… I liked your company… I liked you."

        thalia "But your suffering… and your eyes I can see your pain."

        show ailon worry

        ailon "It won’t work Thalia… plus I don’t wanna make you do this for me..."

        show thalia thinking

        thalia "I’ll just have a few nightmares and it will be over."

        show ailon sad

        ailon "You would do this… for me? Why?"

        show thalia embarrased

        thalia "Because it is what you want right? For your story to end…"

        thalia "It does make me sad… really really sad but it is your wish right?"

        thalia "I think I can... Do something for you."

        show ailon verymad

        ailon "But I haven’t given you anything… you will Be leaving with nothing out of this."

        show ailon surprise

        show thalia angry
        
        thalia "You make it sound like I need something."

        show thalia thinking

        thalia "I don’t, you told me your wish."

        show thalia cutesmile

        thalia "Truthfully..." 

        thalia "And I want to help you."

        show thalia happy at left

        show ailon sweetsmile

        "Ailon looked baffled and then a laugh so loud she couldn’t believe it came from him."

        show ailon smile

        ailon "I have never seen…. That…. Something I haven’t seen in so many years of life, a girl so lovesick as you!"

        show ailon

        show thalia pouts

        thalia "Hey!!"

        "From all the tense and sadness they both laughed in a rare moment of joy."

        show thalia cutesmile

        "And Thalia knew she felt a little tingly feeling."

        show thalia thinking

        "She grasped that moment imprinting in her memory and charged with the knife in hand."

        scene black with fade

        "She didn’t quite feel as the knife hit Ailon, she closed her eyes before hitting him."

        "She heard his voice sweet say."

        ailon "Ya got me…"

        scene bg parknigth

        show thalia angry at smaller,center

        with dissolve

        "She fell to the ground."

        show thalia o

        "As she looked Ailon was no where in sight."

        "Only a small pile of ash"

        show thalia embarrased

        thalia "I hope that made you free… I wish."

        thalia "I just wished we could have had more dates…"

        thalia "Such a shame you were such a cutie…"

        hide thalia with dissolve

        "She cried a whole bunch."

        "Time moved on and so did she."

        "Thalia discovered that all the costumes had turned to dust to, seems that with the curse gone all the immortals were too."

        "Harry made news trying to spill the beans on Ailon, but he was gone with no trace, and so was half the park."

        "Even though the park had lost half its people and Ailon, it seems he had everything in place for it to work without him."

        "Thalia went back to her life, but she carried on her memory those memories with Ailon, she held on to that feeling of kindness despite all the sadness."

        "She went to the park still every now and then, and went on her life, she looked back at it kindly and moved on."

        scene black with fade

        "SELFLESS LOVE ENDING"

        jump end

    label hateRoute:
        
        play music "hbs.mp3"

        "Thalia looked at the gun like it was some alien thing that couldn’t be real."

        show thalia terrified1

        thalia "What… no no no, I can’t take that!"

        show thalia thinking

        harry "Girl… i suggest you do."

        "She was shocked to say the least, and scared he carried one."

        show thalia angry

        thalia "I don’t want it."

        harry "Suit yourself."
 
        "The man kept the gun and pulled out his own and went down the stairs."

        scene bg hallway

        show thalia o at left, smaller

        show harry at center, flip

        with dissolve

        "The place they was a top a catwalk in the service tunnels beneath the park."

        "at bottom the place was poorly lit and the faint sounds of machinery echoed like monster Growls." 

        show thalia confused

        thalia "Wait, who the hell are you? A cop?"

        "Thalia followed the man down the steps into the halls."

        harry "I was… but I retired."

        thalia "And you are here why?"

        harry "Trying to catch this Ailon bastard… he and his family."

        thalia "What you mean?"

        show thalia o

        harry  "I'm not surprised you don’t know, my own family has been after these thugs for more than a generation."

        show harry smile

        thalia "Why?"

        harry "Back when my own grandfather was still your age, he and his wife met one of the Olmenah…"

        show thalia confused

        thalia "Olme… who?"

        show harry -smile

        harry "Girl you don’t even know his surname?"

        show thalia embarrased

        thalia "It’s only our second date."

        harry "Well make it your last, cause this man is hiding something."

        "Harry turned around a corner, his gun aimed, Thalia followed him even more disturbed and confused."

        show thalia o

        harry "Anyhow, both my grandfather and his wife met with one of the Olmenah, they were both enthralled by him, just like you are by this man."

        harry "His wife one day ran away, you could say it’s a classic one, wife gets stollen by a good looking man but my grandfather never saw his loved one again."

        harry "You can say it was vengeance, but he went to look into the Olmenah family and he found out no one ever saw more then one of the families members at a time."

        harry "He thought it was suspicious and the harder he tried to look information the more he hit a brick wall."

        show thalia confused

        thalia "So he thought someone from Ailon's family did something to her? Couldn’t she have run off somewhere?"

        harry "We didn’t think so… I mostly helped my grandad, my father thought he was obsessed."

        harry "The thing is after years we noticed... Their faces never change."

        show thalia o

        thalia "Whose?"

        harry "The Olmenah! This Ailon you have met is the same one my grandfather met."

        show thalia disgust

        thalia "You are crazy, he should be an old man like you!"

        harry "That’s what I’m here trying to find out girl!"

        show thalia angry

        thalia "You are insane… I’m leaving."

        show phobion idle at right
        
        show thalia verysurprise

        "As she turned to leave one of the full suit mascots came walking."

        "She recognized the as the one for earlier in the day."

        phobion "You cannot be here you both… a quest cannot be here."
 
        "Harry pulled Thalia's arm putting her behind him and screamed."

        show thalia o

        harry "Stay where you are."

        "He held out the gun and Thalia froze in fear watching this scene but she still managed to mutter."

        show thalia terrified1

        thalia "No don’t hurt him…"

        phobion "I must say… that is a dangerous toy. You would you put it down?"

        show white 

        play sound "gunshot.mp3"

        show black with fade

        "There was a loud bang and flash, Harry shot the gun right at phobions knee."

        "The man fell back and Thalia was horrified she let out a scream falling on her back."

        show thalia terrified2

        harry "I told you to stay put."

        "Thalia was a bout to run when she saw Phobion stand up like nothing and draw his sword."

        "It was a blunt instrument as a fake weapon, there was this stand off for a few seconds till Phobion charged."

        hide black
        
        show white 

        play sound "gunshot.mp3"

        show black with fade

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade

        "Harry shot his gun at least 4 or 5 times before Phobion came tumbling down at his feet."

        hide white

        hide phobion idle with dissolve

        hide black with dissolve

        show thalia terrified3
        
        thalia "What did you do?!"

        show thalia terrified2

        "Harry had a smirk as he bend down to stage suit and ripped the helmet."

        show thalia terrified3       

        "Underneath was a horrifying sight, human flesh meshed together with metal, his features stretched over metallic composites and whirring."

        harry "See this! He is a sick fuck I knew it."

        "He kicked Phobion and turned to Thalia."

        harry "Here let me help you…"

        "He helped her up and away from phobion's body."

        "Thalias mind was spinning, had she been dating a serial killer? A sadistic psychopath that does this to people."

        harry "Ya sure you don’t want the gun?"

        show thalia terrified1

        thalia "I… think I do."

        "He pulled out the gun and gave it to her, she took the thing still a bit hesitant but more then afraid for her life."

        "She walked in silence behind Harry her mind a mess, a few tears rolling down he cheeks." 
        
        show thalia bigDisgust

        "She begun asking herself how she got in this situation and how she wished she never met Ailon."

        "Soon Harry was using the card to open door."
        
        "Till eventually they found a room."

        show bg repair
        
        with dissolve

        "It looked like an operating room, and in the corner was a man much like Phobion."

        "Half his body was stripped from flesh, instead metal limbs and whirring, there was scans of his brain."

        "There was drawings of his brain being impaled and messed much in the fashion of old lobotomies, Thalia couldn’t bear to look at it."

        "Harry on the other hand pulled out a camera and begun taking pictures."

        show thalia confused
        
        thalia "What even is this…"

        harry "I have no clue, but is more than enough to put him behind bars."

        thalia "Why do this?"
        
        show thalia disgust

        harry "Girl, he is a monster there is no reasoning."

        "She could agree, no one in their right mind would do this to people, if they were even alive."

        "Again she felt sick and could barely stand till she heard Ailons voice."

        show ailon verymad at right
        with dissolve

        ailon "You should not have come here…"

        show thalia surprise

        "Thalia turned, she was so scared she accidentally shot the gun and it hit the ground, the recoil made it fly out of her hand."

        "Ailon didn’t even seem to care, his face a mixture of sadness and anger."

        "Harry took position and aimed his gun."

        harry "You fucking bastard!"

        "I have evidence now… you're going to rot you sick fuck."

        ailon "Harry, why didn’t you leave me alone I have nothing against you."

        harry "I need no reason to bring a monster to justice."

        ailon "You don’t understand!"

        harry "Understand that you a demon?! A Cold Blooded Killer!"

        show thalia bigDisgust

        "Ailon looked at Thalia, its was disgusting to look at him."

        "Once she saw and attractive young man, but now saw a psychopath that tried to buy her affection and it made her sick, she took a step back."

        show ailon sad

        harry "I’m talking to you! Don’t lay a hand on the girl!"

        ailon "I’m sorry… I can’t let you walk out of here."

        harry "Shame…"

        show white 

        play sound "gunshot.mp3"

        show black with fade

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade

        hide ailon

        hide thalia
        
        show harry at right, reverseFlip

        with dissolve

        "Without hesitation he shot twice, one at Ailons Chest and one in his head, Ailon fell to the ground."

        "Behind him rushed Phobion, alive."

        "Thalia was completely frozen in pure shock, and took Harry even a moment to process, he tried to shoot him."

        hide black

        show white 

        play sound "gunshot.mp3"

        show black with fade

        "The first shot went flying and in the second click the gun was empty, he had not reloaded."

        "Phobion jumped Harry brandishing the fake sword and hit Harry in the neck so hard a crack sounded across the room."

        "Thalia was sure, he died on the spot."

        "Then Phobion just stood over the body, his grimaced human semblance, robotic murderous image thaila wished never to see but it was very real."
        
        scene bg repair

        show thalia terrified1 at left, smaller

        show ailon sad at right

        with dissolve

        "Ailon the stood up and the bullet fell from his head and chest just as the wounds closed."

        "Thalia fell to her knees at the impossible sight."

        "Ailon looked at her a measure of pity and shame."

        ailon "I’m sorry… you had to see this."

        show thalia terrified2

        thalia "What… how…"

        show ailon side

        ailon "It’s a dreadful curse really."

        ailon "Are you okay?"

        show ailon worry

        show thalia bigDisgust

        thalia "Get away from me!"

        "She crawled back at a wall away from him."

        ailon "You may not believe me but I tried to help these people… please let me explain."

        thalia "Explain what?!"

        show thalia terrified1

        thalia "That you skin people and keep them in a amusent park!? That you tried to buy me?!"

        show thalia surprise

        thalia "Oh my god… you were going to do the same to me…"

        ailon "Thalia no I…"

        show thalia disgust

        thalia "Don’t say my name! You're fucking sick!"

        ailon "Thalia please…"

        "His expression was utterly sad and shameful and that made Thalia explode."

        show ailon veryworry

        thalia "Oh please don’t make that suffering face!"

        show thalia angry

        thalia "You are sick in the head, you once made me fall for that but now I see you!"

        show thalia bigDisgust

        thalia "A monster! Don’t you dare make that face you sick fuck!"

        "His expression changed to one of surprise, then anger."

        show ailon verymad

        ailon "You have no idea of my suffering! I am not what you think!"

        thalia  "I have seen enough!"

        "She looked around for the gun, she reached for it, grabbed it and aimed at Ailon"

        "He was surprised enough not to move as she shot him, her hands felt the power of the recoil, her eyes filled with light and the air lingered the smell of gun powder."

        show thalia surprise

        show ailon sad

        "Ailon flinched at the shot, but the bullet was simply expelled out and his wound closed."

        "Thalias adrenaline flushed in her veins, she couldn’t kill him."

        show ailon veryworry

        ailon "I know that look…. Thalia please."
 
        "She couldn’t think, what would he do to her?"

        "Who was him? what was this place? why did she even agree to this? and she regretted in a burst out a mad laughter."

        "Till only one thought filled her mind, what if he made her into one of those things in the suits?"

        show thalia thinking

        thalia "Were these people you knew?"

        ailon "People I loved…"

        show thalia bigDisgust

        thalia "your love is sick."

        "She turned the gun on herself and pulled the trigger."

        show white 

        play sound "gunshot.mp3"

        show black with fade

        "HATRED ENDING"

        jump end

    label pityRoute:

        hide harry

        show thalia o

        "The woman took Thalia only a little distance away and pointed out to an employee only entrance."

        employee "Just go through there, down the stairs and to the repair room."
        
        "The woman then gave Thalia a polite nod and walked away."        

        show thalia thinking

        thalia "Right… the repair room."

        show thalia confused

        "Thalia felt confused, she looked at the door, then to the card in her hands."

        "There was a small console beside the door so she swiped the card and the door unlocked."

        show thalia thinking

        "Hesitant she walked in."

        scene bg hallway

        with dissolve

        "It was was a catwalk overlooking a maintenance hallway, the place was filled with pipes and wiring, it was an unsettling view."

        "Thalia heard the door close, then open again for a moment, she looked but there was no one, only some soda crates near by."

        show thalia o at smaller, center with dissolve

        thalia "I don’t really think I should be here but oh well…"

        "She shrugged and walked down the stairs, the ground floor of the hallway had rails where automated carts delivered goods around the park."

        "She couldn’t hear any noise from the park itself, only some mechanical machine sounds and liquids flowing in the pipes."

        show thalia thinking

        thalia "Right… repair room… but where…"

        "Thalia was uneasy the place was by itself weird, she chose to go left."

        "She walked to another intersection, she thought to herself she would get lost here before she found this repair room."

        scene bg repair

        show thalia o at smaller, left 
        
        with dissolve

        "Fortunately for her as she looked around the intersection on one side standing in the middle of the hallway was Phobion."

        "Thalia approached carefully."

        show phobion idle at right

        with dissolve

        thalia "Phobion… you okay?"

        "Phobion turned and it seemed he stood right in front of a cart that darted forward the moment he stepped away, she did too."

        "But back in the intersection a voice complained and the sound of a crash."

        show thalia at center, flip

        show harry smile at left, flip

        "Thalia backed away towards Phobion and a man made around the corner."

        phobion "Fair lady from earlier the day… who is the farthest gentleman from us?"

        show thalia confused

        thalia "I don’t… know, who are you mister?"

        "The man simply laughed and pulled out a gun."

        play music "hbs.mp3"

        show thalia surprise

        anon "You monsters get down on your knees."

        "Thalia was first shocked her whole body froze in place, at the sight."

        hide thalia

        show thalia surprise at right, smaller, flip

        show phobion at center

        with dissolve

        phobion "This is not a toy to wave around, brave gentleman, put down at once."

        show white

        show black with fade

        hide black

        "The man shot the gun in the roof, the loud bang rippled across the halls."

        show thalia terrified1

        "In was enough to make Thalia let a scream of panic."

        hide thalia 

        show phobion at right

        with dissolve

        phobion "I warn only once my great gentleman, or I shall draw my blade against thee."

        show harry -smile

        anon "Oh yeah? Fucking creep!"

        show white

        show black with fade

        "The man shot at Phobion’s leg, Thalia looked horrified as Phobion came to one knee and the man said."

        anon "Try it now."

        "Thalia kneeled down to try and help but she was surprised to see Phobion get up as if nothing happened."

        "A small blood clot forming on his leg, still Phobion pulled out his rapier, it was this blunt metallic prop that was something you could buy in store."

        "The man looked surprised, but it was hard to tell."

        anon "Try it… and this time I kill you boy."

        phobion "I fear no failure."

        "And again to Thalia's horror Phobion charged the man."

        show white

        show black with fade

        show white

        show black with fade        

        "The gun roared fire and lead in response, at least three or four shots, all which hit Phobion."

        "He did not stop, he charged the man without fear, and plunged the prop into the man’s torso."

        "It was a metal still, blunt, yet with enough force, it could hurt someone and that it did."

        "Only when Thalia saw the sword impale the man did she manage to close her eyes in fear."

        "There was the sound of something falling, likely the man’s body, then a few steps followed by a similar yet heavier sound."

        scene bg repair

        show thalia surprise at right, smaller, flip

        show phobion idle at left, flip

        with dissolve

        play music "Lavender.ogg"

        "When she opened her eyes, she saw in the further distance the man impaled, dead, she avoided but saw Phobion close."

        show thalia terrified1

        thalia "Oh my… oh my god… oh shit…"

        "She hesitated but walked to him and turned his body around."

        "There were some bullets wounds in his chest, yet very little blood."

        thalia "I need to find help I…"

        hide thalia

        show thalia o at center, flip, smaller

        with dissolve

        "Phobion grabbed her hand as she made the move to stand up."

        phobion "You do not have to, I shall live through this danger."

        show thalia surprise

        thalia "No… you… you were shot! You need help!"

        phobion "Fair lady I will not perish here, but do help me sit, I need but moment of rest."

        "Hesitant Thalia helped him sit, leaning against the wall, she tried not to look at the dead man in the distance."

        show thalia pouts

        thalia "At least… let me take a look at it maybe I can improvise some bandages."

        phobion "There is no need…"

        show thalia o at reverseFlip

        "She ignored him and she grabbed the suit carefully, pulling clothing."

        show thalia terrified1 at flip

        "She froze when what she saw was flesh fused with machine parts, there was only a small entry wound of the bullet, no blood was flowing like it had almost healed already."

        "Yet it was a horrific sigh, his flesh was cut where cables and metallic joints met flesh and muscle."

        "Phobion grabbed the torn clothing and covered the exposed inside." 

        phobion  "Fear not, I am fine."

        show thalia shout

        thalia "Who… who did this to you?!"

        phobion "Beloved Ailon has seen it so."

        show thalia angry

        thalia "What… why!? "

        "Thalia felt her heart drop, could sweet Ailon hurt people like this, could she be next?"

        phobion "He did so to help myself."

        show thalia shout

        thalia  "How is that helping?!"

        "There were sounds of small pellets hitting the ground, she looked and saw the bullets had been expelled from his body."

        show thalia o

        phobion "My life is one to be forever lady, shots will not kill me! Neither will blades or time!"
 
        "Her mind began racing many questions, but mostly she was happy he seemed okay."

        show thalia confused

        thalia "But… why are you in this state."

        phobion "Oh unfortunately that is something beyond my knowledge hoho! Only Ailon can say."

        thalia "So you don’t know why?"

        phobion  "Only that I have been here a long time!"

        thalia "And you can’t leave?"

        show thalia o

        phobion "I choose to stay, for Ailon, he be lonely if no one was near."

        "Thalia remember how sad and lonely he looked, now she wanted to talk to him and ask personally."

        thalia "Then I need to find him!"

        phobion "I think i know he must should be near the plaza I can take you the way."

        thalia "Are you sure you can… walk?"

        "He got up in a strange fashion but seemed fine."

        phobion "Nothing will ever stop courage and honor!"

        show thalia cutesmile

        "Thalia laughed"

        hide thalia

        show thalia surprise at right, flip , smaller

        with dissolve

        "She tried to look at the dead man but Phobion put himself between them."

        show thalia confused

        phobion "Do not think of it, I shall solve this evildoers fate, you have done no wrong."

        show thalia thinking

        "That made her feel bad but she also didn’t want to look at it, she hesitated but began walking the other way."

        phobion "I also… believe I have been most blunt I my manners… may I ask this fair lady name?"

        show thalia o

        thalia "It’s Thalia."

        phobion "It good to know… I should tell the others too."

        thalia "There are other people like you? In the park?"

        phobion "That is matter better asked to Ailon not?"

        show thalia thinking

        thalia "Maybe… okay I will."

        scene bg hallway

        with dissolve

        "Phobion took her around the tunnels, they must have walked for some good minutes before they climbed some stairs and were back in the park."

        "Phobion however still had his costume damaged so he stayed inside and said."

        scene bg parknigth with dissolve

        show thalia o at left, smaller

        show phobion idle at right

        with dissolve

        phobion "He should be here, good luck lady Thalia… and please be kind to him… I remember him a kind soul."

        show thalia thinking

        thalia "I… will try."

        hide phobion with dissolve

        "Phobion went back and Thalia looked around for Ailon."
     
        show thalia o

        "She saw him sitting down alone, he seemed confused and sad."

        "She mustered the courage to walk to him."

        thalia "Hey Ailon…"

        show ailon surprise at right

        "He seemed startled by her voice and looked at her confused."

        thalia "We should talk…"

        show ailon sad

        ailon "I…  thought you were back there still… how did you find me?"

        show thalia thinking

        thalia "Phobion said you would be here…"

        show ailon verymad

        ailon "You… talked to Phobion?"

        "Ailon seemed to be slightly more serious that it was a bit scary when he spoke."

        ailon "And what did you talk about?"

        show thalia angry

        thalia "He told me some things… about himself and you… but I thought I should ask myself."

        ailon "Okay just… keep here and don’t move… I mean it."

        hide ailon with dissolve

        "Ailon looked very serious it was almost scary."

        "He then stood up and talked to some of the staff, then blocked part of the plaza and told people it was under maintenance."

        "The park was already closing and there were only people far away now, and they were alone."

        show ailon at right with dissolve

        ailon "What exactly happened?"

        "Ailon was serious and there was also some anger in his voice."

        "Thalia was surprised to see him that way but after what happened she was even more confused."

        show thalia o

        thalia "I went after Phobion… to ask him about you… and well a man followed me, when I found Phobion he pulled a gun on us."

        show ailon verymad

        "Ailons posture changed as he focused his attention."

        ailon "Did he hurt you?"

        show thalia thinking

        thalia " No… Phobion I think he… he might have killed him…"

        show ailon worry

        ailon "Killed him?!"

        show thalia angry

        thalia  "He was trying to shot at him."

        show ailon -worry

        ailon "Where is he now?"

        show thalia confused

        thalia "I don’t really know, down the maintenance tunnels, Phobion didn’t let me look a second time."

        "Ailon looked like he was about to get up but Thalia grabbed his arm."

        show thalia thinking

        thalia "Phobion also got shot… but he lived… I saw underneath his clothes too."

        show ailon veryworry

        "Ailons eyes twitched, a mix of shame, surprise and fear, Thalia didn’t know which was stronger so she continued." 

        show thalia disgust

        thalia "He said he was immortal… that I should ask you… Ailon what is going on?"

        show ailon sad shadow

        "Ailon took a deep breath and his eyes almost swelled with tears."

        show ailon side -shadow

        ailon "He did not lie… he is… and so am I."

        show thalia surprise

        "Thalia was surprised to say the least, first she did not believe but then she saw a man get shot and get up like nothing."

        thalia "How?!"

        show thalia o

        show ailon sad

        ailon "I was cursed, a very long time ago, to live forever…"

        thalia "How long…"

        ailon "Longer than I would like."

        thalia "What you mean by that?"

        show ailon verymad shadow

        ailon "Thalia I have been around since man lived in caves!"

        "Thalia got scared for a moment at his outburst as he continued to spill his fury."

        ailon "And I can’t stand anymore."

        ailon "I have seen more then I would like to see."

        ailon "You wanted to know what Phobion had to tell you?!"

        ailon "I cursed him too, so has mostly every poor soul in this park!"

        ailon "They were once people I loved but are now shells of themselves."

        show ailon sad

        ailon "And I can’t take it anymore!"

        show thalia at center with dissolve
        
        "He fell to his knees crying and Thalia rushed to him sitting down in the ground with him."

        thalia "It’s okay… I don’t think I understand all of it but I see you…"

        show thalia surprise at left with dissolve

        show ailon verymad

        ailon "No you don’t…"

        "He pushed her."

        ailon "His body I did that!"

        ailon "I had too, they all go mad with their immortality! It was the only way to keep him safe."

        ailon "And I had to do it…"

        show ailon sad

        ailon "So many times..."

        ailon "I’m an immortal being who trapped the people he loved in metal sarcophagus like broken toys I’m a monster!"

        show thalia o

        thalia "You are suffering!"

        show ailon verymad

        ailon "Yes, Thalia, I am!"

        ailon "Because this life…. This damn mind and body keeps me alive and sane unlike all the people I love."

        show thalia thinking

        thalia "Is there no way to end it?."

        ailon "The only way to do it is if someone who loves me selflessly used a knife to kill me."

        "Thalia was puzzled, yet everything about this day was weird, she imagined it was part of the curse so she yelled."

        show thalia angry

        thalia "Bring the knife here then!"

        show ailon -shadow surprise

        ailon "What?"

        thalia "I like you… despite what you said I still do… let me try!"

        show ailon verymad

        ailon "Are you insane?!"

        thalia "To try and help someone?"

        show thalia pouts

        ailon "By stabbing me?"

        thalia "You don’t die do you?"

        ailon "It still hurts like a bitch."

        show thalia o

        show ailon sad

        "There was strange pause..."

        show ailon cutesmile

        show thalia sweetsmile

        "And an awkward laugh between the two."

        show thalia happy

        thalia "Bring it here… I have seen a lot today.. I want to help."

        ailon "You are unbelievable…"

        show ailon sad

        show thalia angry

        "Thalia felt a bit angry at his comment but also proud."

        "Yet felt this whole thing was almost unreal."

        "Ailon got up his expression seemed very sad."

        hide ailon

        show thalia o

        with dissolve

        "Thalia reached out her hand as he left to get the knife, but she neither reached it nor could say anything."

        "A few moments passed and she was all alone in the plaza."

        show thalia thinking

        "Her head filled with thoughts of the day."

        "She did still, despite all think kindly of Ailon, she wanted to help him, if that somehow had to end with his end maybe it was for the best."

        "But she also did not want that, she wanted to spend more time with him, to know him better to understand his view."

        "Her thoughts cut short when he came back carrying a very old knife."

        "It looked like something you would see in a museum, it seemed fashioned from a dark rock with a leather grip."

        show ailon at right

        show thalia o

        ailon "I have it here…"

        "She could see in his face doubt, shame but maybe a hope this could give him what he wanted."

        show thalia confused

        thalia "So that knife… made you and the others… imortals?"

        show ailon sad

        ailon "Yes…"

        thalia "And you make people imortal by being stabbed? Who even came up with that?"

        ailon "If you know, do tell me… I have some complaint to them."

        "Again Thalia looked awkward at the object and at him not knowing exactly what to say."

        "Ailon took a step and handed her the knife taking again a step back."

        show ailon verymad

        ailon "Do it fast… just in the stomach… it don’t hurt as bad and easier to strike"

        show thalia thinking

        thalia "You seem to know."

        ailon "Not the first time I tried it…"

        show thalia angry

        "Thalia was hesitant, would it work? She couldn’t know, was he insane? Maybe but it seems it was what he wanted."

        "She looked at him, he close his eyes in a serene way and braced."

        "Thalia thought she wanted to spend time with him and this could be the end of it."

        "So she decided on a new course of action."

        "Ailon heard a striking sound and a welp not his own, opening his eyes Thalia had stabbed herself."

        scene black with fade

        show ailon worry shadow with dissolve

        ailon "No!"

        "He rushed to her cradling her head."

        "She gave him a sad look as desperation spread across his face, but then her eyes had a kind manner."

        thalia "Now I’ll be immortal too… and you won’t be alone."

        show ailon veryworry

        ailon "No Thalia it had to be me to do it! You are just gonna die like this!"

        thalia "Oh… I didn’t know… guess I’m silly."

        "If he said anything she hear only echos."

        "She felt her body get cold but then a sharp pain on her neck."

        "Her conscience seemed to fade, like melting deep in a river."

        "Then she felt hot and burning sensation and a jolt of pain made her sit down and scream."

        scene bg parknigth

        show thalia disgust at left, smaller

        with dissolve   

        thalia "Oh shit! Ouch!"

        show ailon worry at right

        "She looked as Ailon sat just across from her his head down, the knife in his hands and bloodied."

        "She touched her stomach and the wound was gone but she felt her clothes a bit soggy with blood, her neck too."

        show thalia confused

        thalia "Did you?"

        ailon "I killed you… before you bled out yourself… now you are…"

        thalia "Immortal?"

        show ailon sad

        ailon  "I’m sorry…."

        "He began to cry almost child like and Thalia again hugged him saying."

        show thalia angry

        thalia "Ailon you saved me from my own self stupidity, I’m fine."

        show ailon verymad

        ailon "No you are not! Don’t you get it."

        "He stood up."

        ailon "You cannot live forever you will lose your mind! I have condemned you to live like a shell till the end of time! All because I was too weak…"

        show ailon sad

        ailon "To let you die…"

        thalia "You are not weak! You are kind!"

        show ailon verymad

        ailon "Kindness has nothing to do with this! It’s fact."

        ailon "The human brain can’t retain information after certain time, in 100 years you won’t be yourself anymore."

        thalia "I won’t! I’ll be here still."

        show ailon sad shadow

        ailon "I… I’m done… then do just that."

        show thalia o

        "His whole silhouette seemed to grow tired and weary, completely devasted."

        "It lasted only a moment but in the next."

        show ailon sweetsmile -shadow

        "He beamed a smile, almost to perfect to be honest but it did fool Thalia that she thought his saddens turned to relief."

        ailon "Lets make the best then, of the years to come!"

        show thalia cutesmile

        "Thalias heart was relieved and she smiled kindly at him as she made the decision to stay by his side."

        show thalia happy

        thalia "I’m glad I got through your thick skull."

        hide thalia

        hide ailon

        with dissolve

        "The man that Phobion killed went unnoticed, and not even the police came looking for him, apparently it was deemed a missing person and there was nothing linking him to the park."

        "Whatever he came here to do, he did it in secret and it was his undoing."

        "Thalia lived along with Ailon for many years helping in the park, going on dates."

        "She did try using the knife but it never worked, but they were happy nonetheless."

        "Until about 150 years later Thalia seemingly lost interest in living things, she began with animals, Ailon did not notice… but the change and trail of blood soon could not be hidden."
        
        scene black with fade
        
        "SELFISH LOVE ENDING"
        jump end
        
    label end:
    
    return