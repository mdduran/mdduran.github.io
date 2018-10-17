# You can place the script of your game in this file.
    init:
        python:
            import maze
            import mazedifficult
  
  
  #Last edit: Matt, adding character images and replacing the swear-words with *'s in the censored version, added hobo
  #9/29/13
  #edited by marco 9/30/13 10:01 pm added difficulty function
  #edited by mark 10/1/13 6:43 pm added new script to both censored and uncensored , fixed some mistakes
  #edited by matt 10/11/2013 to test the dodge minigame.
  #edited by matt 10/13/2013 6:47 PM. Fixed bugs: Multiple hobo assassinations, police station hat, day counter bug. added forcefield to burger scene.
  #edited by matt 10/14/2013 9:00 PM. Censored version.
  
  #code for censored version starts on line 3210
  
  
    define weirdness = 0
    define evepissed = 0
    define difficulty = 0
    define day = 0
    define daysleft = 0
    define money = 0
    define knowledge = 10
    define statuedestroyed = 0
    define evedate = 0
    define choice8b = True
    define burgers = 0
    define hat = 0
    define hobo = 0
    define bank = 300
    define assassin = 0
    
    
    
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    image bg apartmentday = "apartmentday.png"
    image bg apartmentnight = "apartmentnight.png"
    image bg apartmentsunset = "apartmentsunset.png"
    image bg bank = "bank.png"
    image bg alley = "alley.png"
    image bg bookstore1 = "bookstore1.png"
    image bg bookstore2= "bookstore2.png"
    image bg burgerstore= "burgerstore.png"
    image bg burgerstoreplaypen = "burgerstoreplaypen.png"
    image bg cityoverview = "cityoverview.png"
    image bg citysidewalk= "citysidewalk.png"
    image bg citystatue = "citystatue.png"
    image bg citystatuedestroyed = "citystatuedestroyed.png"
    image bg crypt= "crypt.png"
    image bg graveyardday= "graveyardday.png"
    image bg graveyardnight= "graveyardnight.png"
    image bg nightclub= "nightclub.png"
    image bg jail= "jail.png"
    image bg policestation= "policestation.png"
    image bg death = "dead.png"
    image box nextlocation = "NextLocationBox.jpg"
    image bg title = "title.png"
    image bg credit = "credits.png"
    image bg credit2 = "credits2.png"
    
    image forcefield normal = "forcefield.png"
    image explosion normal = "explosion.png"
    
    image boss normal = "mob_boss_normal.png"
    image boss happy = "mob_boss_happy.png"
    image boss angry = "mob_boss_angry.png"
    
    image bankteller normal = "bankteller.png"
    
    image bryant normal = "bryant_normal.png"
    image bryant happy = "bryant_happy.png"
    image bryant angry = "bryant_angry.png"
    image bryant sad = "bryant_sad.png"
    image bryant shooting = "bryant_shooting.png"
    image bryant shootingfinger = "bryant_shootingfinger.png"
    image bryant punch = "bryant_punch.png"
    image bryant scared = "bryant_scared.png"
    image bryant gun = "bryant_gun.png"
    image bryant side1 = "bryant_side.png"
    
    image bryant animated:
        "bryant_shooting.png" 
        pause .2
        "bryant_gun.png" 
        pause .2
        repeat
    image bryant animated2:
        "bryant_normal.png"
        pause .5
        "bryant_happy.png"
        pause .5
        repeat
        
    image citizen normal = "citizen_normal.png"
    
    image eve normal = "eve_normal.png"
    image eve happy = "eve_happy.png"
    image eve angry = "eve_angry.png"
    image eve punch = "eve_punch.png"
    
    image gangster normal = "gangster_normal.png"
    image gangster happy = "gangster_happy.png"
    image gangster angry = "gangster_angry.png"
    image gangster gun = "gangster_gun.png"
    image gangster shooting = "gangster_shooting.png"
    image gangster animated:
        "gangster_gun.png"
        pause .2
        "gangster_shooting.png"
        pause .2
        repeat
        
    image gangster2 normal = "gangster2_normal.png"
    image gangster2 happy = "gangster2_happy.png"
    image gangster2 angry = "gangster2_angry.png"
    image gangster2 gun = "gangster2_gun.png"
    image gangster2 shooting = "gangster2_shooting.png"
    image gangster2 animated:
        "gangster2_gun.png"
        pause .2
        "gangster2_shooting.png"
        pause .2
        repeat
    
    image hobo normal = "hobo_normal.png"
    image hobo happy = "hobo_happy.png"
    image hobo angry = "hobo_angry.png"
    
    image magicianred casting = "spellcastingred.png"
    image magiciangreen casting = "spellcastinggreen.png"
    image magicianblue casting = "spellcastingblue.png"
    image magicianyellow casting = "spellcastingyellow.png"
    
    image magicianred normal = "magician_red.png"
    image magicianyellow normal = "magician_yellow.png"
    image magicianblue normal = "magician_blue.png"
    image magiciangreen normal = "magician_green.png"
    image magician normal = "magician_nohat.png"

    
    image policeman normal = "policeman_normal.png"
    image policeman shooting = "policeman_shooting.png"
    image policeman angry = "policeman_angry.png"
    
    image burgerdude normal = "burgerdude_normal.png"
    
    
    # Declare characters used by this game.
    define e = Character(_('Bryant Day'),
                        color="#006400",
                        window_left_padding=160,
                        show_side_image=Image("bryant_side.png", xalign=0.0, yalign=1.0))
    define l = Character(_('Eve'),
                        color="#00ffff",
                        window_left_padding=160,
                        show_side_image=Image("eve_side.png", xalign=0.0, yalign=1.0))
    define h = Character(_('Hobo'),
                        color="#bdb767",
                        window_left_padding=160,
                        show_side_image=Image("hobo_side.png", xalign=0.0, yalign=1.0))
    
    define c = Character(_('Customer'),
                        color="#ff8c00",
                        window_left_padding=160,
                        show_side_image=Image("citizen_side.png", xalign=0.0, yalign=1.0))
    define g = Character(_('Gangster'),
                        color="#a52a2a",
                        window_left_padding=160,
                        show_side_image=Image("gangster_side.png", xalign=0.0, yalign=1.0))
    define g2 = Character(_('Gangster 2'),
                        color="#bdb767",
                        window_left_padding=160,
                        show_side_image=Image("gangster2_side.png", xalign=0.0, yalign=1.0))
    define mb = Character(_('Mob Boss'),
                        color="#bdb767",
                        window_left_padding=160,
                        show_side_image=Image("mob_boss_side.png", xalign=0.0, yalign=1.0))
    define m = Character(_('Magician'),
                        color="#ff0000",
                        window_left_padding=160,
                        show_side_image=Image("spellcastingred_side.png", xalign=0.0, yalign=1.0))
    define m2 = Character(_('Magician'),
                        color="#ffd700",
                        window_left_padding=160,
                        show_side_image=Image("spellcastingyellow_side.png", xalign=0.0, yalign=1.0))
    define m3 = Character(_('Magician'),
                        color="#000080",
                        window_left_padding=160,
                        show_side_image=Image("spellcastingblue_side.png", xalign=0.0, yalign=1.0))
    define m4 = Character(_('Magician'),
                        color="#7fff00",
                        window_left_padding=160,
                        show_side_image=Image("spellcastinggreen_side.png", xalign=0.0, yalign=1.0))
    define p = Character(_('Police Officer'),
                        color="#00008b",
                        window_left_padding=160,
                        show_side_image=Image("policeman_side.png", xalign=0.0, yalign=1.0))
    define b = Character(_('Burger Dude'),
                        color="#696969",
                        window_left_padding=160,
                        show_side_image=Image("burgerdude_side.png", xalign=0.0, yalign=1.0))
    define bt = Character(_('Bank teller'),
                        color="#ff4500",
                        window_left_padding=160,
                        show_side_image=Image("bankteller_side.png", xalign=0.0, yalign=1.0))
    

# The game starts here.
    label start:
        scene black
        "Which difficulty would you like to play?"
        menu:
            "Difficulty: Normal":
                $ difficulty = 0
                $ daysleft   = 7
            "Difficulty: Hard":
                $ difficulty = 1
                $ daysleft   = 5
                
        "May contain frequent and intense realistic violence, frequent and intense mature, horror, and suggestive themes; also strong sexual content, nudity, strong language, alcohol, tobacco, and drugs which may not be suitable for children under the age of 18."
        "Please confirm that you are 18 or older. If not,you can play the censored version of the game."
        menu:
            "I am older than 18":
                jump choice0_old
            "I am younger than 18":
                jump choice0_young
                
                
                
    label choice0_old:                            #If older than 18
        play music "main.ogg"
        scene bg apartmentday
        show bryant normal
        "This is Bryant Day; He’s an average man, living an average life in an average city with an average job."
        "He’s mediocre, undistinguishable, ordinary, unremarkable, indifferent, lackluster, and forgettable."
        "And he’s proud of it."
        scene bg citysidewalk 
        show hobo angry at right
  
    
        "Bryant kept his head down all his life; He stays out of fights, keeps an average amount of friends, watches all the popular shows, eats only typical food."
        "If ever there was a standard for the most average human in existence, Bryant would have the high score."
        init:
            $ move = MoveTransition(1.0)
        show bryant normal at offscreenright with move
        show bryant normal at right with move
        show bryant normal at center with move
        show bryant normal at left with move
        "He aims to stay at the top. Well, not the very top: he can’t get too good at something."
        scene bg bookstore2
        show bryant normal at left
        show eve normal at offscreenright 
        "Here, as an average retailer in an average bookstore, Bryant Day wi-"
        show eve normal at right with move
        show eve normal at center with move
        l "Bryant, help me sort these new books out. I already know where most of them are going."
        "That’s Bryant’s best friend, Eve."
        "She’s the manager of this store, and has practically memorized everything there is to know about the store's inventory."
        l "Bryant, what are you doing?"
        e "Just having an internal monologue about how awesomely average my life is."
        l "…Whatever I guess."
        show eve normal at right with move 
        show eve normal at offscreenright with move
        "She’s a bit too smart for Bryant’s taste, but not everyone can be as average as himself."
        "But here, as an average retailer in an average bookstore, Bryant Day will live out the rest of his average life in an average manner."
        "He will retire after an average number of years to raise an average number of children,"
        "and die at the average life expectancy, forever to rest in an average grave."
        "Hooray for low expectations!"
    
        "At least, that’s the plan."
        #Marco: 10/6/2013 at 11:54 AM made grammatical changes to script thus far.
        play music "energetic_music.ogg"
        
        show magicianred normal behind bryant:
            xalign .9 yalign .7
        show magicianblue normal behind bryant:
            xalign .7 yalign .7
        show magiciangreen normal behind bryant:
            xalign .5 yalign .7
        show magicianyellow normal behind bryant:
            xalign .3 yalign .7

        
        m "This is an outrage!"
        e "What can I help you with s-"
        m2 "Those ingrates at the so called “magician shop” across the street dare to call themselves first rate when they don’t even have a spare supply of Ether to sell!"
        m2 "They're trying to give me a gimmick along with just magic wands and those barely enchanted playing cards. Why I had better tools when I was just a wee lad playing with dolls!"
        m3 "Next time, we will NOT be buying anything in their shop, let me tell you."
        e "That is interesting but also seems irrelevant."
        m4 "Quite true, unlike the blatant false advertising etched into this book we purchased."
        e "\" Dolls and Boys: Psychological studies on a young one’s development cycles\" What was wrong with it?"
        m4 "It only talked about the humans growing up or something, nothing at all about the doll’s thoughts at all."
        m4 "There always seems to be an unfair bias towards humans in these kind of books."
        m "I suspect racism!"
        m2 "We demand reparation in the form of what we expected!"  
        m3 "Some form of writing regarding the mental state of the Homo Mannequinious!"
        e "Wait, are you trying to return this? The receipt says it’s from Borders, and they went out of business a while ago."
        m "Blatant racism!"
        m2 "See here, petty mortal, the inner workings of puppets and mannequins could span eons worth of physical pages, and with a rich history that could possibly dwarf all of your \"modern era\"."
        m2 "They’re quite good conversationalists as well, I would know."
        m3 "I’ve been talking to puppets since I was born."
        m3 "Enough of your ignorant prattle, not having any tomes on this glorious matter would be a shame to this establishment and anyone within eyeshot of it."
        e "I just checked our records, and I really don’t think we have any books concerning a subject that doesn’t exist."
        "..."
        m "You dare to belittle our glorious art?"
        m "After all the countless perfect puppets we’ve created?"
        m "Do you suggest that there’s nothing to write about their wonderful and completely existent thought process?"
        m2 "Are you mad?"
        m3 "Perhaps he’s mocking us out of jealousy..."
        m4 "Or maybe out of fear..."
        m "Regardless of your motives, your implied ignorance is an affront to our very lifework."
        m "If you’re so insistent that a puppet is mindless let’s see how you feel being one!"
        show magicianred casting behind bryant:
            xalign .9 yalign .7
        show magicianblue casting behind bryant:
            xalign .7 yalign .7
        show magiciangreen casting behind bryant:
            xalign .5 yalign .7
        show magicianyellow casting behind bryant:
            xalign .3 yalign .7
        play sound "spell.ogg"
        "..."
        e "Anything else I can help you with?"
        m2 "Not really I guess. We appreciate the quick service."
        m "But we’ll be back in a century or two, be sure to expand your inventory by then."
        e "Sure thing, sir."
        show magicianred normal at offscreenright with move
        show magicianblue normal at offscreenright with move
        show magiciangreen normal at offscreenright with move
        show magicianyellow normal at offscreenright with move
        play music "main.ogg"
        e "Well then, that was very un-average."
        e "But who cares, I guess..."
        show eve normal at right with move
        l "If you’re done talking with those un-average gentlemen, could you carry an average amount of average books to their respectively average piles already?!"
        e "I can use synonyms, if it’s starting to get on your nerves."
        scene black with dissolve
        "Tap to continue ..."
    
    #Marco: edited more errors on 10/6/2013 4:44 pm
    

    
    
        scene bg apartmentnight
        show bryant normal
        e "Well, besides those weirdoes, it was another perfectly average day."
        e "Now, time for an average night’s sleep."
        scene bg apartmentnight with dissolve
        scene black with dissolve
        #stop music 
        play sound "spell.ogg"
        #pause
        scene black with dissolve
        "Tap to continue..."
    
        scene bg apartmentday
        show bryant normal
        e "Looks like another gloriously ordinary day is afoot."
        e "I guess I’ll -"
        menu:
            "sleep in a little.":
                jump choice1_sleep
            "go out to work.":
                jump choice1_work
        label choice1_sleep:
            $ weirdness += 1
            scene bg apartmentday
            show bryant angry
            e "fall back asleep? I usually head out to work now, but I guess I’m too tired."
            scene black with dissolve
            pause 3.0
            scene bg apartmentday 
            show bryant angry
            e "Oh poop, now I’m late! I shouldn’t have wasted so much time in bed!"
            jump choice1_done
        label choice1_work:
            jump choice1_done
            label choice1_done:
                
            scene bg citysidewalk
            show bryant normal at left
            show hobo normal at right
            e "Oh geez, that beggar is still here."
            h "Hey you, got any change?"
        menu:
            "Just keep walking to work.":
                jump choice2_walkaway
            "Give him some pocket change.":
                jump choice2_givemoney
            "Tell him to get a job.":
                jump choice2_getajob
        label choice2_walkaway:
            jump choice2_done
        label choice2_givemoney:
            $ weirdness += 1
            show hobo angry at right
            h "What, just this? Gimmie a 10, I’ve fought in every war there was!"
        menu:
            "Walk away.":
                jump choice3_done
            "Give him $10 more.":
                jump choice3_more
            "Tell him to go earn it.":
                jump choice3_getajob
        label choice3_more:
            $ weirdness += 1
            e "Fine, here’s another $10."
            show hobo happy at right
            h "About darn time someone gave me the respect I deserve. *grumble grumble*"
            e "Why did I do that? I’ve been ignoring him for months now."
            jump choice3_done
        label choice3_getajob:
            jump choice2_getajob
        label choice2_getajob:
            $ weirdness += 1
            e "Why don’t you go earn it, you dirty beggar?"
            show hobo angry at right
            h "You’re more dirty than me, you ungrateful little runt! *grumble grumble*"
            e "Why did I say that? I’ve been ignoring him for months now."
            jump choice2_done
            label choice3_done:
                jump choice2_done
            label choice2_done:
        
            scene bg bookstore1
            show bryant normal at left
            if (weirdness > 0):
                e "Well, now that I’m here, at least the rest of the day will go normally."
            else:
                e "I’ll have to make this day twice as average as usual, to make up for yesterday."
            e "Here comes a customer now."
            show citizen normal at offscreenright with move
            show citizen normal at right with move

            c "Excuse me, do you know where the history section is?"
                #Marco: just gunna leave a suggestion here, in the beginning of the scene, just show bryant then after he says his two lines, have the customer enter the scene on the right.
        menu:
            "Tell him where it is.":
                jump choice4_normal
            "Insult him for being so helpless.":
                jump choice4_insult
            "Recommend a better subject than history.":
                jump choice4_subject
        label choice4_normal:
                e "Right over there, sir. You can see the sign from here."
                c "Ah, thank you."
                jump choice4_done
        label choice4_insult:
                $ weirdness += 2
                e "Under the big sign that says history, dumba**."
                c "Well, I never!"
                show bryant normal at left with move
                show bryant normal at offscreenleft with move
                c "Wait, What?!?"
                jump choice4_done
        label choice4_subject:
                $ weirdness += 1
                e "Nobody cares about history nowadays, try going to the cooking section over there instead."
                c "Uh, um, er..."
                show citizen normal at right with move
                show citizen normal at offscreenright with move
                e "Wait, why would I say that?"
                jump choice4_done
        label choice4_done:
                scene bg bookstore2
                show bryant normal at right
                show eve normal at left
                l "Bryant, you're not working with any customers, right? Come help me with these books."
        menu:
            "Help her.":
                jump choice5_normal
            "Don’t help her.":
                jump choice5_bad
            "Tell her off.":
                jump choice5_vbad
        label choice5_normal:
                e "Sure, as long as my part is as average as it was yesterday."
                l "You never shut up about averageness, do you?"
                e "It’s my thing. Why can’t you accept me for the average man I am, Eve?!"
                l "Be quiet, you!"
                jump choice5_done
        label choice5_bad:
                $ weirdness += 1
                e "Eve, you do realize I’m paid to work the register around here right? Not heavy lifting!"
                show eve angry at left
                l "What?"
                l "I only have a few books left, it’ll only take a second if you help me."
                e "It's not in my job description."
                l "Whatever, jerkwad."
                e "Wait, what the hell?! I’ve always been helping Eve with chores!"
                e "What’s gotten into me?"
                jump choice5_done
#Marco: fixed grammatical errors up to here on 10/6/2013
        label choice5_vbad:
                $ weirdness += 2
                $ evepissed += 1
                e "Eve, why don’t you do my job for a change? You're always expecting me to drop everything I’m doing for your convenience!"
                "..."
                show eve angry at left
                l "What the heck, Bryant!? I was the one who recommended you to the manager in the first place, and now you’re suddenly an ungrateful ba***** who can’t deign to carry a few books between customers?"
                l "Fine then, f*** you. A**hole."
                e "What the heck!? Eve is my best friend, why did I insult her like that?"
                jump choice5_done
        label choice5_done:
            if (weirdness == 0):
                scene bg apartmentsunset
                show bryant normal
                e "Seems today was another average day after all. Those weirdoes couldn’t corrupt my averageness after all."
                e "Everything turned out all right, I guess..."
                e "Now, to repeat until I die of old age."
                stop music
                play music "scary_music.ogg"
                scene bg death
                pause
                jump choice0_done
            elif (weirdness < 4):
                scene bg apartmentsunset
                show bryant normal
                e "That’s so odd, I was doing some really uncharacteristic things today."
                e "Now that I think about it, I couldn't even remember my train of thought when I was doing these actions. It’s like I just felt a random impulse and did it."
                e "It seems unlikely, but maybe those magician weirdoes did something to me when they were casting that spell?"
                e "I mean, maybe they secretly drugged me or something while they pretended to ‘cast a spell’ on me? I can’t think of anything else that could have made me do that stuff."
                e "I have the rest of the week off, I guess I can look up more about them in my spare time."
                e "Actually, maybe Eve knows about them."
                e "I remember she saw them, she might even know more about that doll cult or whatever they were blabbing about."
                e "First thing tomorrow, I’ll go to the book-store and ask her about it."
                scene black
                "Tap to continue ..."
                play sound "spell.ogg"
            elif (weirdness >= 4):
                scene bg apartmentsunset
                show bryant normal
                e "Okay, what the hell?!"
                e "I could never imagine myself doing half those things, but I just did them all at the same time, and I don’t even know why."
                e "It’s like I just got these random impulses to do irregular things, and I did them without thinking about it until afterwards."
                e "This is freaky and dangerous. I feel like I don’t have control over what I’m doing anymore."
                e "Wait! Those magician weirdoes yesterday, didn’t they cast some sort of puppet spell on me?"
                e "I’d never believe in unaverage junk like that working in a million years, but could my random actions today possibly be proof? I’ve got to be sure!"
                e "I have the rest of the week off..."
                e "I know Eve saw them, maybe she saw what they were doing when the magicians were pretending to cast a spell on me."
                e "I’ve got to ask her about it tomorrow. For now, I’ve got to rest my mind from all of this disgusting unaverageness."
                scene black with dissolve
                "Tap to continue ..."
                play sound "spell.ogg"
            screen example_imagemap:
                            imagemap:
                                ground "cityoverview.png"
                                hover "cityoverviewfocused.png"

                                hotspot (216, 212, 124, 42) action Return("bookstore")
                                hotspot (328, 140, 124, 42) action Return("alley")
                                hotspot (354, 328, 124, 42) action Return("apartment")
                                hotspot (460, 188, 124, 42) action Return("bank")
                                hotspot (465, 48, 124, 42) action Return ("burgerstore")
                                hotspot (328, 22, 124, 42) action Return ("cemetary")
                                hotspot (454, 386, 124, 42) action Return ("sidewalk")
                                hotspot (626, 444, 124, 42) action Return ("statue")
                                hotspot (598, 342, 124, 42) action Return ("nightclub")
                                hotspot (184, 346, 124, 42) action Return ("policestation")
                            text ("Days left: %d" % (daysleft)) size 30 xalign 0.5 yalign 0.99
                            text ("Hats collected: %d" % (hat)) size 25 xalign 0.5 yalign 0.9
                            #ui.text("Days Left: %(daysleft)d", size=40, xalign=0.5)
        
        
            label map:
    
                                call screen example_imagemap
    
                                $ result = _return
    
                                if result == "bookstore":
                                    scene bg bookstore1 
                                    show bryant normal at left
                                    e "It’s my week off, but I’m still allowed to come here of course."
                                    e "Now that I’m here, I’ll..."
                                    label bschoice_a:
                                        scene bg bookstore1
                                        show bryant normal at left
                                        menu:
                                            "Go back outside":
                                                e "Go right back outside. Ok then."
                                                jump map
                                            "Go see Eve":
                                                jump choice14_eve
                                            "Read some books ":
                                                jump choice14_books
                                            "Work":
                                                jump choice14_work
                                            "Set the whole Bookstore on fire ":
                                                jump choice14_fire
                                        label choice14_eve:
                                            e "Eve, it’s me."
                                            if (evepissed >= 1):
                                                show eve angry at right
                                                l "What do you want, asshole?"
                                                e "Oh right, I pissed her off yesterday, didn’t I?"
                                            else:
                                                show eve normal at right
                                                l "Bryant? I thought it was your week off."
                                            e "Eve, I-"
                                            label bschoice_b:
                                            menu:
                                                "Run away":
                                                    e "Gotta go fast!"
                                                    show bryant normal at left with move
                                                    show bryant normal at offscreenleft with move
                                                    if (evepissed >= 1):
                                                        l "Damn right you run..."
                                                        jump map
                                                    else:
                                                        l "That’s unaverage of him..."
                                                        jump map
                                                "Explain the situation ":
                                                    e "I need your help."
                                                    if (evepissed >= 1):
                                                        l "No."
                                                        e "Eh? But I-"
                                                        l "No. Fuck off."
                                                        e "But I’m-"
                                                        l "NO."
                                                        e "Women are so weird..."
                                                        e "Uh, ok, but still I-"
                                                        jump bschoice_b
                                                    else:
                                                        l "With what?"
                                                        e "This is going to sound strange, but do you remember those magician weirdos with the hats I was talking to before?"
                                                        l "Yeah, they were pretty memorable. What about them?"
                                                        e "I think they cast a spell on me or something. I keep doing things I don’t want to do and I can’t control myself."
                                                        l "That sounds more like a medical condition, probably brought on by your unhealthy obsession with being average."
                                                        l "It’s probably the unique spirit inside you yearning to be set free."
                                                        e "No way, I murdered that little guy years ago. It has to be a mystical curse or something."
                                                        l "Well, try reading up on them. I overheard the part where they said we need more books on doll mythology or something, so I ordered a few."
                                                        menu:
                                                            "Go read them":
                                                                e "I’ll go check them out right now. Thanks a lot Eve."
                                                                l "No problem."
                                                                jump choice14_books
                                                            "Ask for cliffnotes":
                                                                jump choice15_notes
                                                        label choice15_notes:
                                                            e "You’ve already read them, right? Can you just summarize them for me?"
                                                            l "Eh? I did read them, but I’m working now."
                                                            l "I can’t just-"
                                                            e "Eve, I was probably cursed by those guys. Come on, I don’t have time."
                                                            l "Ugh... Jerk."
                                                            l "Well, for a really short summary..."
                                                            l "There was, like, a branch of alchemists back in the middle ages who thought, since they could turn stone into gold, they should be able to transform dolls into humans somehow and make the perfect person."
                                                            l "But it turned out they couldn’t, so they tried turning people into puppets instead, which sounds like brainwashing."
                                                            e "Oh geez."
                                                            l "It’s all a load of shit, I’ve already put it in the fiction section."
                                                            e "Did it say anything more about the brainwashing part?"
                                                            l "Uh, I think so. It said they figured something out, but they always had to kill the brainwashed guy after a while. Apparently all the power from their hats ran out or something if they let him go."
                                                            
                                                            e "Oh."
                                                            e "Oh crap."
                                                            l "You can read it yourself if you have the time; I don’t think anyone’s going to buy books like that anytime soon."
                                                            e "Yeah, thanks Eve."
                                                            l "... I’ll go back to work, then."
                                                            show eve normal at right with move
                                                            show eve normal at offscreenright with move
                                                            if (knowledge == 0):
                                                                $ knowledge += 1
                                                                e "Oh shit, that sounds dangerously similar to what I’m going through. Except I haven’t died..."
                                                                e "...Yet."
                                                                e "I gotta find those magicians. Maybe they can break the curse early or something."
                                                                e "For now, I’ll-"
                                                                jump bschoice_a
                                                "Tell her everything is all right":
                                                    e "I am completely fine and not in any trouble at all."
                                                    l "..."
                                                    l "Is that so?"
                                                    e "Yeah, everything is totally average."
                                                    l "..."
                                                    if (evepissed >= 1):
                                                        l "Then fuck off."
                                                    else:
                                                        l "So you just came here to annoy me in your free time?"
                                                        e "Yeah pretty much"
                                                        l "Go away."
                                                    e "But also, I-"
                                                    jump bschoice_b
                                                "Confess to her ":
                                                    e "I..."
                                                    e "Eve, I can’t control myself any longer."
                                                    if (evepissed == 3):
                                                        play sound "punch.ogg"
                                                        show eve punch at right
                                                        pause
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done
                                                    elif (evepissed == 1):
                                                        l "..."
                                                    else:
                                                        l "...?!??"
                                                    e "I’ve always enjoyed talking with you..."
                                                    e "You’ve been with me here since day one, and I thought I would be happy with us just being friends..."
                                                    if (evepissed == 1):
                                                        l "..."
                                                    else:
                                                        l ".............."
                                                    e "But lately, you’ve grown to be something more to me. Something important."
                                                    if (evepissed == 1):
                                                        l "..."
                                                    else:
                                                        l "And?"
                                                    menu:
                                                        "Propose to her":
                                                            jump choice16_propose
                                                        "Ask to go out with her ":
                                                            jump choice16_askout
                                                        "Ask to borrow some money ":
                                                            jump choice16_money
                                                        "Tell her it was a joke ":
                                                            jump choice16_joke
                                                        "Ask her to be your best friend ":
                                                            jump choice16_bf
                                                    label choice16_propose:
                                                        if (evepissed >= 1):
                                                            e "WILL YOU MARRY M-"
                                                            play sound "punch.ogg"
                                                            show eve punch at center
                                                            pause
                                                            scene bg death
                                                            stop music
                                                            play music "scary_music.ogg"
                                                            pause
                                                            jump choice0_done
                                                        else:
                                                            e "WILL YOU MARRY ME?"
                                                            l "..."
                                                            l "..."
                                                            l "..."
                                                            l "... No."
                                                            e "OK..."
                                                            e "Kill me now."
                                                            e "Also, I-"
                                                            jump bschoice_b
                                                    label choice16_askout:
                                                        e "Will you go out with me?"
                                                        if (evepissed >= 1):
                                                            l "No. Fuck off."
                                                        elif (evedate == 1):
                                                            l "I already said yes."
                                                            e "Oh, right."
                                                            e "..."
                                                            e "Also, I-"
                                                            jump bschoice_b
                                                        else:
                                                            l "Sure, I guess."
                                                            e "Sweet."
                                                            l "Not while I’m on duty though..."
                                                            l "We’ll talk later when it’s my day off."
                                                            e "When's that?"
                                                            l "I’ll call you."
                                                            e "Sure thing."
                                                            e "You rock, unknown omnipresent puppeteer wingman dude!"
                                                            $ evedate == 1
                                                            e "Also, Eve, I-"
                                                            jump bschoice_b
                                                    label choice16_money:
                                                        e "Can I borrow some cash?"
                                                        l "..."
                                                        e "I wouldn’t ask this from anyone else but you."
                                                        l "..."
                                                        e "Just like 10$, you cheap bit-"
                                                        play sound "punch.ogg"
                                                        show eve punch at center
                                                        pause
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done
                                                    label choice16_joke:
                                                        e "I‘m just kidding."
                                                        l "..."
                                                        e "LOL the look on your face..."
                                                        if (evepissed <= 1):
                                                            l "Fuck off, asshole."
                                                            e "Hahaha,"
                                                            e "MAN I’m funny."
                                                            l "Fuck. Off."
                                                            $ evepissed == 3
                                                            e "Oh, also, I-"
                                                            jump bschoice_b
                                                        else:
                                                            play sound "punch.ogg"
                                                            show eve punch at center
                                                            pause
                                                            scene bg death
                                                            stop music
                                                            play music "scary_music.ogg"
                                                            pause
                                                            jump choice0_done
                                                    label choice16_bf:
                                                        e "Will you be my best friend?"
                                                        if (evepissed >= 1):
                                                            l "…No."
                                                            e "Aww maaan."
                                                            e "Also, I-"
                                                            jump bschoice_b
                                                        else:
                                                            l "…What?"
                                                            e "Like right now we’re just friends, right? Can we be best friends?"
                                                            l "…What’s the difference?"
                                                            e "Idk. Actually I don’t think I’m friends with anyone else, so you’re kinda my best friend by default..."
                                                            l "… I hate you."
                                                            e "No you don’t, best friend. Anyway, I-"
                                                            jump bschoice_b
                                                "Amuse her":
                                                    e "I am the meanest guy around."
                                                    if (evepissed >= 1):
                                                        l "..."
                                                    else:
                                                        l "… Oh really?"
                                                    e "You deny it now? After I’ve been declaring it out loud all my life?"
                                                    if (evepissed == 1):
                                                        l "..."
                                                        l "Oh."
                                                        l "you... mean..."
                                                        l "... as in average."
                                                        l "..."
                                                        e "HA, you smiled."
                                                        l "..."
                                                        e "Come on, cheer up from whatever I did. Even an average guy like me has an upper and lower range."
                                                        l "... Shut up."
                                                        e "You’re smiling again. My batting average is 2 for 2 so far!"
                                                        l "... Heh, you moron."
                                                        e "It's hard to deviate from our average relationship isn’t it?"
                                                        l "I guess so."
                                                        e "Great."
                                                        e "I guess that calmed her down a bit."
                                                        e "Also, Eve, I-"
                                                        jump bschoice_b
                                                    else:
                                                        l "…Oh, I get it."
                                                        e "Mean as in average."
                                                        e "Mathematics also one of your many areas of expertise then?"
                                                        l "Of course."
                                                        e "Figures. Also, I-"
                                                        jump bschoice_b
                                        label choice14_books:
                                            e "Go read some books. It’s a bookstore, after all."
                                            scene bg bookstore2
                                            show bryant normal at left
                                            e "Hmm, what to read?"
                                            label bschoice_c:
                                                menu:
                                                    "Go back to the entrance":
                                                        e "Eh, I’ll head back to the entrance."
                                                        jump bschoice_a
                                                    "Read some Shakespeare ":
                                                        jump choice17_shakespeare
                                                    "Read some cooking recipes ":
                                                        jump choice17_cooking
                                                    "Read about dwarves abusing quantum mechanics ":
                                                        jump choice17_dwarves
                                                    "Read up on magicians ":
                                                        jump choice17_magicians
                                                label choice17_shakespeare:
                                                    "“To die, to sleep- to sleep, perchance to dream- ay, there’s the rub, for in this sleep of death, what dreams may come…”"
                                                    e "I don’t get it, so was this guy sleepy or emo? And who was he rubbing? Wait no, was someone rubbing him? Is that what he’s on about?"
                                                    e "Overhyped. Probably paid for all those rave reviews. Ugh, next..."
                                                    jump bschoice_c
                                                label choice17_cooking:
                                                    "“1: Place water and rice in microwave-safe bowl. If desired, add tub margarine and salt to taste. 2: Cover. Microwave on high for ~5 minutes, or more per serving. 3: Let stand 5 minutes or until water is absorbed. Fluff with fork.”"
                                                    e "Wow, this is a lot better than history. Next..."
                                                    jump bschoice_c
                                                label choice17_dwarves:
                                                    "“It is unclear exactly how two (or more) mechanisms talk to each other at a distance without building direct mechanical or electronic channels between them (such as a wire), and given that the Dwarves have not discovered radio technology, it is believed by some that the Dwarves have actually discovered how to implement and control quantum entanglement on a non-quantum scale.”"
                                                    e "...."
                                                    e "Wait, uhhh.."
                                                    e "Um..."
                                                    e "..."
                                                    jump bschoice_c
                                                label choice17_magicians:
                                                    if (knowledge == 1):
                                                        e "“This must be the book eve was talking about. I’ll skim through it”"
                                                    e "“After successfully perfecting the technique of altering base substances to higher forms (Commonly remembered for the stone to gold example), the alchemists sought to elevate the human form instead.”"
                                                    e "“This proved too difficult a feat with their limited resources, and internal conflicts lead to a schism; The alchemists continued into Europe to profit off their current knowledge, but a small number obsessed with creating a perfect form diverged into the new continent, calling themselves ‘Magicians’ instead”"
                                                    e "“This sect explored the possible connections between the human form and that of the perfect template, puppets, and if their mystic powers could somehow forge a stable connection between the two”"
                                                    e "Oh man, this must be it. Lets see, anything about magic spells?"
                                                    e "“... spells were very taxing, and the subjects that were often subject to forces outside of their control, causing them to wander off with the mages power still held within them. To solve this problem, most common rituals included a low costing lethal, but reversible curse that would cause the subject to die after %(daysleft)d days.”"
                                                    e "“The effort required to reverse the curse became inefficient as the number of subjects for testing rose dramatically; it became second nature to simply have domination spells kill off the subject after a week or so.”"
                                                    e "Oh no. Ohhh nooooooo..."
                                                    e "But, it said it was reversible, do I have a chance?"
                                                    e "“… reversing domination is a long and complex process, requiring counterchants lasting at least 3-4 lengths longer than the original hyme, also including a mirror of recursive scrying,”"
                                                    e "“... underneath the full moon... requires at least 500gp worth of components... must rest for 1-4 days afterwards...”"
                                                    e "Cmon, I’m trying to save my life here, I don’t need this nerd shit."
                                                    e "“...or alternatively collect the focus of power for each person involved in the original casting, usually an article of clothing or magical item that holds deep symbolism / importance to the owner, and adorn them yourself.”"
                                                    e "there we go... that means..."
                                                    e "I just have to collect their ‘power focuses’, which is... uh.."
                                                    e "It has to be their hats! That’s it! I collect their hats before this time limit is up, and I won’t die from the curse!"
                                                    $ knowledge == 2
                                                    scene bg bookstore1
                                                    show bryant normal at left
                                                    e "But now I’ve got to find them, and I don’t have any leads."
                                                    e "Hmm, I’m not really sure what I should do next."
                                                    e "I guess I’ll-"
                                                    jump bschoice_a
                                        label choice14_work:
                                            e "Go work some overtime."
                                            e "Can’t have enough extra cash, I suppose."
                                            show citizen normal at offscreenright with move
                                            show citizen normal at right with move
                                            c "Excuse me, do you work here?"
                                            e "Yes, I do."
                                            c "Great. Can you direct me to the history section?"
                                            scene black
                                            "*Many boring hours later*"
                                            scene bg bookstore1
                                            show bryant normal at center
                                            e "Feels just like the good old average days again."
                                            e "Except the rates on my time off are lower, ugh."
                                            e "Still, 100$ is 100$"
                                            $ money += 100
                                            e "Everyone else already went home. No choice but to head back home."
                                            jump apartmentn
                                        label choice14_fire:
                                            show policeman normal at offscreenright with move
                                            show policeman normal at right with move
                                            e "Just set the whole bookstore on fire, I guess."
                                            p "ARE you now?"
                                            e "I guess I a-"
                                            e "..."
                                            e "Why is there a policeman in the bookstore?"
                                            p "Are policemen not allowed to buy books?"
                                            e "..."
                                            p "You’re under arrest."
                                            e "On what charges?"
                                            p "Premeditated arson, but mostly blatant racism."
                                            e "Wondering why a cop is eavesdropping on me in the middle of a bookstore is blatant racism?"
                                            p "“Why would a cop be in a bookstore? I thought pigs couldn’t read.”"
                                            e "I didn’t say that!"
                                            p "That’s what it sounded like to me. It’s always “What is a policeman doing here? Shouldn’t he be out giving parking tickets like the rest of his little buddies? Why are you in my house?”"
                                            p "Well how about now? I caught an arsonist in the act!"
                                            menu:
                                                "Surrender quietly":
                                                    e "Ok, you caught me. Now what?"
                                                    p "I’ll just bring you to the station, and you’ll have to watch a presentation to learn about the importance of being a better member of the community."
                                                    e "That’s it? I was going to burn down this Bookstore for no discernable reason."
                                                    p "The presentation is about 7 hours long. If you survive, the community spirit will be burned into your skull, and whatever’s left of you is free to go."
                                                    e "Oh god... Please no..."
                                                    scene black
                                                    "*7 hours later*"
                                                    jump apartmentn
                                                "Deny the charges ":
                                                    jump choice18_deny
                                                "Kick him and run for it ":
                                                    jump choice18_kick
                                            label choice18_deny:
                                                e "But I didn’t actually do anything, I just said I was going to."
                                                p "You think words can’t hurt people? Cops have feelings too you know. And they can read. I read a lot."
                                                e "Yes, I’m sure, but I’m just saying I didn’t actually do anything illegal enough to be arrested."
                                                p "Don’t change the subject, racist."
                                                p "And quit going on about that."
                                                p "..."
                                                p "I’m watching you."
                                                e "You were before, too."
                                                show policeman normal at right with move
                                                show policeman normal at offscreenright with move
                                                e "Hmph. Now then, I’ll-"
                                                jump bschoice_a
                                            label choice18_kick:
                                                e "Uh, think fast!"
                                                p "Are you implying cops can’t thin-OW"
                                                show bryant normal at left with move
                                                show bryant normal at offscreenleft with move
                                                pause
                                                scene bg citysidewalk
                                                show bryant normal at right
                                                e "I think I lost him!"
                                                e "Wait, I just attempted to burn down the place I work at and then assaulted an officer to escape arrest!"
                                                e "I’m gonna have to go on an average spree after this curse thing gets sorted out..."
                                                jump map
                                                

                                                        
                                                
                                            
                                            
                                            
                                    jump map
                                elif result == "alley":
                                    scene bg alley
                                    show bryant normal
                                    e "Oh! What am I doing here?"
                                    e "I should probably get out before I get raped!"
                                    jump map
                                elif result == "apartment":
                                    label apartmentn:
                                        scene bg apartmentnight
                                        show bryant normal at center
                                        if (hat == 0) and (knowledge == 0):
                                            e "(Well, I’m still no further to finding out about this whole curse thing.)"
                                            e "(Maybe I’ll get to it tomorrow, then.)"
                                            e "Asking Eve about those weirdos seems like my only option at this point.)"
                                        elif (hat == 0) and (knowledge == 1):
                                            e "(Now I know that it’s really a curse they put on me, but I still don’t know much about it.)"
                                            e "(Maybe I should have read the books)"
                                            e "(Or I could just find a magician and ask him to undo it, I guess)"
                                        elif (hat == 0) and (knowledge == 2):
                                            e "(Another day wasted, and I’ve still got to find those magicians before it’s too late.)"
                                            e "(I’m not even sure where they all are at this point)"
                                            e "(I gotta hurry up.)"
                                        elif (hat == 1):
                                            e "(I’ve got one hat now, but I still need to get the other three.)"
                                            e "(That first magician said one of his friends liked food or something, didn’t he?)"
                                            e "(The only place for food I can think of is that burger store downtown.)"
                                            e "(I’ll get to it tomorrow, I hope.)"
                                        elif (hat == 2):
                                            e "(I’ve got two hats now, but I still need two more to undo the curse.)"
                                            e "(I’ll need to get them pretty quick)"
                                            e "(that time limit is coming soon.)"
                                        elif (hat == 3):
                                            e "(Only one more hat to go, totally final battle shit goin on. )"
                                            e "(I can hardly wait)"
                                            e "(I’ll finally be able to go back to being average again.)"
                                        scene black
                                        "Tap to continue..."
                                        $ day += 1
                                        $ daysleft -= 1
                                        if (daysleft <= 0):
                                            play sound "spell.ogg"
                                            scene bg death
                                            stop music
                                            play music "scary_music.ogg"
                                            pause
                                            "Bryant ran out of time."
                                            jump choice0_done
                                        else:
                                            scene bg apartmentday
                                            show bryant normal
                                            e "Yawn ..."
                                            e "Looks like another"
                                            e "disgustingly erratic day, with this curse controlling my every move."
                                            e "Oh well, time to find a way to break it!"
                                        jump map
                                elif result == "bank":
                                    scene bg bank
                                    show bryant normal at left
                                    show bankteller normal at right
                                    e "Wait, the bank? What do I need at the bank?"
                                    bt "Can I help you, sir?"
                                    label bankchoice:
                                        menu:
                                            "Leave the bank":
                                                e "Nope, thanks for the offer."
                                                bt "Enjoy your day then."
                                                jump map
                                            "Start a conversation ":
                                                jump choice23_conv
                                            "Make a deposit / withdraw ":
                                                jump choice23_make
                                            "Check your balance ":
                                                jump choice23_balance
                                            "Rob the bank ":
                                                jump choice23_rob
                                        label choice23_conv:
                                            e "Nice weather we’re having, isn’t it?"
                                            bt "Uh, yes, yes it is."
                                            e "Not that I can tell, I haven’t looked upwards in a while now."
                                            e "That and most people don’t seem to have feet, for some odd reason. And it looks like everyone is talking without moving their lips."
                                            bt "Excuse me, but this seems more like a medical condition on your part, sir."
                                            e "I’d go to the hospital, but it’s not one of the options on that map thing I keep seeing. I doubt they could cure the weirdness a group of magicians cast on me a few days ago anyways."
                                            bt "Uh... um... anything more, banking related, I could help you with sir?"
                                            jump bankchoice
                                        label choice23_make:
                                            e "I’d like to access my account, please."
                                            bt "Certainly, what for?"
                                            menu:
                                                "Deposit all your money":
                                                    jump choice24_depa
                                                "Deposit 100$":
                                                    jump choice24_depb
                                                "Do nothing ":
                                                    jump choice24_none
                                                "Withdraw 100$ ":
                                                    jump choice24_witha
                                                "Withdraw all your money ":
                                                    jump choice24_withb
                                            label choice24_depa:
                                                e "I’d like to deposit all my money."
                                                if (money == 0):
                                                    bt "Erm, what money, sir?"
                                                    e "Oh, right. Nevermind."
                                                    bt "Uh, anything else I can help you with?"
                                                    jump bankchoice
                                                else:
                                                    $ bank += money
                                                    $ money = 0
                                                    bt "Right away. You now have a total of %(bank)d in your savings."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice
                                            label choice24_depb:
                                                e "I’d like to deposit 100$"
                                                if (money == 0):
                                                    bt "Erm, what money, sir?"
                                                    e "Oh, right. Nevermind."
                                                    bt "Uh, anything else I can help you with?"
                                                    jump bankchoice
                                                else:
                                                    $ money -= 100
                                                    $ bank += 100
                                                    bt "Right away. You now have a total of  %(bank)d in your savings."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice
                                            label choice24_none:
                                                e "Nevermind."
                                                bt "Oh, ok then…"
                                                bt "Anything else?"
                                                jump bankchoice
                                            label choice24_witha:
                                                e "I’d like to withdraw 100$"
                                                if (bank < 100):
                                                    bt "It seems you don’t have 100$ in your account, sir."
                                                    e "Darn it. Nevermind, then..."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice
                                                else:
                                                    $ money += 100
                                                    $ bank -= 100
                                                    bt "Right away. You now have a total of %(bank)d in your savings."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice
                                            label choice24_withb:
                                                e "I’d like to withdraw all my money."
                                                if (bank == 0):
                                                    bt "It seems your account is completely empty, sir."
                                                    e "Really? That sucks."
                                                    bt "Indeed. Anything else I can help you with?"
                                                    jump bankchoice
                                                else:
                                                    $ money += bank
                                                    $ bank = 0
                                                    bt "Right away. You now have no savings."
                                                    e "Yolo."
                                                    bt "Right..."
                                                    bt "...anything else I can help you with?"
                                                    jump bankchoice
                                                
                                        label choice23_balance:
                                            e "I’d like to check my account balance."
                                            bt "Lets see, Bryant Day correct? You have %(bank)d dollars saved up here."
                                            e "(and I have %(money)d on hand)"
                                            bt "Anything else I can help you with today?"
                                            jump bankchoice
                                        label choice23_rob:
                                            e "I’d like to make a withdraw, actually."
                                            bt "How much, sir?"
                                            show bryant gun at left
                                            e "THE ENTIRE GODDAM BANK. THIS IS A ROBBERY."
                                            bt "Oh god. Sir, please calm down."
                                            e "I’LL CALM DOWN WHEN YOU START HANDING OVER THE CASH!"
                                            bt "Sir, you’re trying to rob a bank in broad daylight with no mask, just calm down and give yourse- "
                                            e "I’M CALM RIGHT NOW. IF YOU DON’T WANT TO SEE ME ANGRY, START HANDING ME THE MONEY RIGHT-FUCKING-NOW."
                                            e "(OhmygodohmygodohmygodwhatamIdoing)"
                                            e "(WHERE DID THIS GUN EVEN COME FROM DID I BRING IT WITH ME AND NOT EVEN NOTICE WHAT THE HELL!)"
                                            p "This is the police, we have you surrounded."
                                            p "At least on this side."
                                            p "Release the hostages and lay down your weapon, NOW."
                                            e "YOU DON’T CONTROL ME, PIGS I’LL-"
                                            menu:
                                                "Surrender":
                                                    jump choice25_surrender
                                                "Waste a hostage ":
                                                    jump choice25_hostage
                                                "Go down in a blaze of glory ":
                                                    jump choice25_blaze
                                                "Make a deposit":
                                                    jump choice25_deposit
                                            label choice25_surrender:
                                                p "Surrender quietly."
                                                p "..."
                                                p "Oh, geez, really? That usually doesn’t work."
                                                p "I mean wow, finally, someone who listens to a cop. I’ve been yelling at people for years, and they all just ignore me."
                                                p "This is great. And I’ll probably get the rest of the day off too."
                                                p "Hell, you’ve learned your lesson, right?"
                                                e "Uh, yeah, totally."
                                                p "You’re not gonna do it again, right?"
                                                e "...Maybe."
                                                p "Tell ya what..."
                                                p "Just go home, get a good nights sleep, think about what you did, and I’ll let you off the hook. OK?"
                                                e "Uh... Yeah, sure."
                                                p "Good man. And a good LISTENER, too. You take care now."
                                                e "Right...see you then."
                                                
                                                jump apartmentn
                                            label choice25_hostage:
                                                p "PROVE IT."
                                                bt "NO, PLEASE, I HAVE A WIFE AND KIDS. MERCY."
                                                bt "HE'S IGNORING THE HOSTAGE AFTER BEING ASKED SO POLITELY. TAKE HIM DOWN!"
                                                play music "gunshot.wav"
                                                show policeman shooting at right
                                                pause
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                            label choice25_blaze:
                                                e "I'M GONNA TAKE YOU ALL DOWN WITH ME."
                                                bt "He’s lost it! Take him down!"
                                                play music "gunshot.wav"
                                                show policeman shooting at right
                                                pause
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                            label choice25_deposit:
                                                show bryant normal at left
                                                e "Make a deposit, please."
                                                bt "Wait, what?"
                                                e "Oh, wait, sorry, are you closed now?"
                                                bt "HE’S LOWERED HIS GUARD. TAKE HIM DOWN."
                                                play music "gunshot.wav"
                                                show policeman shooting at right
                                                pause
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                                
                                                
                                                
                                                
                                                
                                                
                                                        
                                                
                                                                    
                                                                       
                                    
                                    
                                    jump map
                                    
                                    
                                    
                                elif result == "burgerstore":
                                    scene bg burgerstore
                                    show bryant normal at left
                                    show burgerdude normal at right
                                    e "“The burger store, always good to grab a bite to eat when you’re trying to break some freaky mind control curse.”"
                                    b "*sigh* Hello, valued customer, may I take your order?"
                                    label burgerstorea_:
                                        menu:
                                            "Leave":
                                                b "Thank you for your patronage… *sigh*"
                                                jump map
                                            "Order some burgers":
                                                jump choice19_burger
                                            "Order some tacos ":
                                                jump choice19_tacos
                                            "Ask about magicians ":
                                                jump choice19_ask
                                            "Rob the place ":
                                                jump choice19_rob
                                        label choice19_burger:
                                            if (money == 0):
                                                e "I’d like a burger, please."
                                                b "Yes, “sir”. Here you are."
                                                e "Oh, actually it looks like I don’t have any money on me, sorry."
                                                b "*Sigh* I guess we’ll have to throw it out then."
                                                b "Disgusting shit isn’t fit to be eaten anyway. mumble mumble."
                                                e "What was that?"
                                                b "Anything else, sir?"
                                                jump burgerstorea_
                                            $ money -= 5
                                            if (burgers == 0):
                                                $ burgers = 1
                                                e "I’d like a burger, please."
                                                b "Yes, “sir”. Here you are."
                                                e "Thanks! *nomnomnom*"
                                                b "Anything else for you today, “sir”?"
                                                jump burgerstorea_
                                            elif (burgers == 1):
                                                $ burgers = 2
                                                e "I’ll have another burger. A few more, actually."
                                                b "Right away, “sir”."
                                                e "*nomnomnom* Mmm, sooo many burgers. I don’t think I can handle another bite."
                                                b "You probably could, you fucking fatass."
                                                e "What?"
                                                b "I asked if you were going to order anything else, “sir”?"
                                                jump burgerstorea_
                                            else:
                                                $ money -= 100
                                                $ burger = 0
                                                e "I’ll have a few more burgers, actually."
                                                b "How many?"
                                                e "Hmmm…"
                                                e "How many do you have?"
                                                scene black
                                                "*hours later*"
                                                scene bg burgerstore
                                                show bryant angry at left
                                                e "Ughhh... uff... URP."
                                                e "What... what happened?"
                                                b "You were inhaling burgers till you passed out, “sir”."
                                                e "What? How long was I out?"
                                                b "A couple hours, its 11:00 now."
                                                e "11:00?!? I wasted my entire day here!"
                                                e "Wait, I passed out for multiple hours and you just left me here? No ambulance or anything?"
                                                b "They don’t pay me enough to care."
                                                e "... No one else cared?"
                                                b "You think anyone else comes to this place?"
                                                e "Point taken... Ugh... I’m still nauseous."
                                                b "That makes two of us, sir."
                                                e "... I’m leaving."
                                                b "Thank you, come again."
                                                jump apartmentn
                                        label choice19_tacos:
                                            e "I’d like a taco, please."
                                            b "Sir, this is a burger store."
                                            e "Don’t you have some tacos in storage, just in case or something?"
                                            b "No."
                                            e "Could you, like, form burger meat into the filling and make the bun in a taco shape?"
                                            b "No."
                                            e "Uh, could you order tacos for delivery and have me pay you for them?"
                                            b "No."
                                            e "What can you do?"
                                            b "Tolerate morons like you while I work for minimum wage."
                                            e "Barely."
                                            b "Will that be all, valued customer?"
                                            jump burgerstorea_
                                        label choice19_ask:
                                            e "Do you happen to know anything about a group of hat-wearing wizards obsessed with puppets that shout loudly about anything that remotely annoys them?"
                                            if (hat == 0):
                                                b "Sir, are you going to order some mother-fucking burgers or not?"
                                                jump burgerstorea_
                                            elif (hat > 1):
                                                b "Not anymore."
                                                jump burgerstorea_
                                            else:
                                                b "Oh, you know him?"
                                                e "\"Him\"? You mean you know about one?"
                                                b "He’s in the playpen area, and eats more than the usual fatasses, but doesn’t pay for meals, and keeps yammering about dolls and other shit."
                                                e "Really?!? I’ll go talk with him."
                                                jump playpen
                                        label choice19_rob:
                                            e "I’d like to order..."
                                            e "All the money in your register."
                                            b "Sir, that’s not for sale."
                                            e "Uh... I’m robbing you."
                                            b "Sir, robbery is illegal."
                                            e "I know it is, but I’m doing it anyway. Now give me the money or I’ll threaten you a second time."
                                            b "Sir, being a devout believer in reincarnation, the threat of physical violence doesn’t scare me."
                                            b "That, and I’ve stood here for 5 years having to watch disgusting fatasses chug burgers for minimum wage and no hope of advancement."
                                            b "If you don’t do it, I’ll get around to it eventually."
                                            e "Wow, you’re really depressing."
                                            b "I know, right?"
                                            b "So are you gonna order some shit or what?"
                                            jump burgerstorea_
                                        label playpen:
                                            scene bg burgerstoreplaypen
                                            show magicianblue normal at right
                                            show bryant normal at left
                                            show forcefield normal at right
                                            m3 "*Munch, snarf, gobble*"
                                            e "Hey you! Magician!"
                                            m3 "*Crunch* Eh? What do you want, mortal?"
                                            e "You and your buddies cursed me, remember?"
                                            m3 "..."
                                            m3 "Oh, that’s right... I remember you. Curse of the puppet right?"
                                            e "Yeah, and it turns out you forgot about how the curse will kill me if I don’t remove it."
                                            m3 "..."
                                            if(difficulty == 0):
                                                m3 "Oh, that’s right, I remember that, you die after 7 days with it, right?"
                                            else:
                                                m3 "Oh, that’s right, I remember that, you die after 5 days with it, right?"
                                            m3 "..."
                                            e "So hand over the hat!"
                                            m3 "What? No."
                                            e "But I’m going to die without it!"
                                            m3 "So? "
                                            e "Eh?"
                                            m3 "There are like 6 billion of you running around the place. Get over it."
                                            e "Wait, you can’t just ignore me when I’m about to die!"
                                            m3 "*Chew* Watch me, mortal."
                                            label playpenchoice:
                                                menu:
                                                    "Go back to the register":
                                                        jump choice20_register
                                                    "Ask for the hat":
                                                        jump choice20_hat
                                                    "Ask about him ":
                                                        jump choice20_ask
                                                    "Try reverse psychology ":
                                                        jump choice20_psychology
                                                    "Punch him in the face ":
                                                        jump choice20_punch
                                                label choice20_register:
                                                    e "Fine, I’m going back to the register."
                                                    m3 "Whaaatever. *Chomp, munch*"
                                                    scene bg burgerstore
                                                    show bryant normal at offscreenleft
                                                    show burgerdude normal at right
                                                    show bryant normal at left with move
                                                    b "Is he going to pay now?"
                                                    e "Nope, don’t think so."
                                                    b "I’d tell him to get out, but I really don’t care that much."
                                                    e "Apparently."
                                                    e "..."
                                                    jump burgerstorea_
                                                label choice20_hat:
                                                    e "Really, though, can I have your hat?"
                                                    m3 "Nope. *gobble*"
                                                    e "Do I need to pass a test first? Earn it somehow?"
                                                    m3 "No. Go away. *Buuuurp*"
                                                    e "Come on, I gotta get it somehow."
                                                    m3 "Even if I was willing, you couldn’t. I accidentally cast a force field between me and the outside world, so you can’t even come near me if you tried."
                                                    e "What?!? Then how do you keep ordering all those burgers?!?"
                                                    m3 "I ordered all these beforehand, THEN I made the forcefield."
                                                    m3 "Oh, I mean, made it on accident."
                                                    e "Wait, you ordered all those burgers and just made a forcefield around yourself to eat them in peace?"
                                                    m3 "Doesn’t work that well, apparently. I can still hear your whiny little mortal complaints. *crunch, smack*"
                                                    e "So then how are you getting air in there?"
                                                    m3 "There’s actually an entrance over there: I bewitched the playpen tunnels to become a labyrinth that only a masterful wizard could solve, and air can pass through."
                                                    e "So, I could possibly go in there and get your hat if I passed through your labyrinth?"
                                                    m3 "*Chew, snarf* Fine, mortal. Pass my maze and I’ll give you my hat. If and when you can’t, go run away like a good mortal."
                                                    
                                                    label playpenchoices3:
                                                        menu:
                                                            "Run away like a good mortal":
                                                                e "Nevermind, I won’t try it."
                                                                m3 "...Suit yourself.  *Eating noises*"
                                                                jump playpenchoice
                                                            "Try the maze ":
                                                                e "Fine then, I’ll try your maze."
                                                                m3 "*Buuurp* Dinner with a show, this shall be entertaining."
                                                                "Use the arrow keys to move in the maze. Reach the exit before time expires or you’ll be expelled back to the entrance again."
                                                                python:
                                                                    renpy.free_memory()
                                                                    
                                                                    if (difficulty == 0):
                                                                        success = maze.main()
                                                                    else:
                                                                        success = mazedifficult.main()
                
                                                                if success == 1:
                                                                    show bryant happy at right
                                                                    show forcefield normal at right
                                                                    e "HA! I got past your stupid maze! Now we meet face to face."
                                                                    m3 "Oh. Well how about that."
                                                                    e "Now give me your hat!"
                                                                    m3 "... Naw."
                                                                    e "But you said-"
                                                                    m3 "I crossed my fingers."
                                                                    e "... You were eating hamburgers while promising."
                                                                    m3 "Who cares, you’re just a mortal. Get over it."
                                                                    menu:
                                                                        "Demand the hat":
                                                                            jump choice21_hat
                                                                        "Give up and leave ":
                                                                            jump choice21_leave
                                                                        "Punch him in the face ":
                                                                            jump choice21_punch
                                                                    label choice21_hat:
                                                                        e "No! I passed your maze, now give me your hat! A promise is a promise."
                                                                        m3 "*Chew* Promises with wizards are different. We say one thing, but we mean another thing of equal value."
                                                                        e "Eh? So what are you offering me instead?"
                                                                        m3 "Learning a one way teleport spell."
                                                                        e "... That actually sounds pretty useful."
                                                                        m3 "*Gobble* Indeed it is. Watch closely..."
                                                                        show magicianblue casting at right
                                                                        play sound "spell.ogg"
                                                                        pause 2.0
                                                                        hide bryant with dissolve
                                                                        show bryant normal at left with dissolve
                                                                        show magicianblue normal at right
                                                                        e "Wait, I’m just outside the forcefield again."
                                                                        m3 "Yeah, did you see me casting it? I don’t normally give lessons like that so cheap."
                                                                        e "Hey, you can’t get rid of me that easily!"
                                                                        m3 "Just did. *Gulp*"
                                                                        e "Asshole fatty magician grumble grumble..."
                                                                        jump playpenchoice
                                                                    label choice21_leave:
                                                                        e "Fine, I give up."
                                                                        m3 "... So easily? Mortals are such fickle creatures. *Chew*"
                                                                        m3 "As you wish."
                                                                        hide bryant with dissolve
                                                                        show bryant normal at left with dissolve
                                                                        e "Wait, you can teleport me?"
                                                                        m3 "Apparantly."
                                                                        e "Couldn’t you have just teleported me inside, rather than watch me rush through a crazy mystical playpen maze?"
                                                                        m3 "But that was the best part! *Gulp*"
                                                                        e "... Asshole fatty magician grumble grumble…"
                                                                        jump playpenchoice
                                                                    label choice21_punch:
                                                                        play sound "punch.ogg"
                                                                        show bryant punch at center
                                                                        m3 "*Belch* OW! Owwww..."
                                                                        show bryant normal at center
                                                                        e "No more mystical forcefield, eh promise breaker?"
                                                                        
                                                                        m3 "Ugh... Simple barbarian, you trifle with powers beyon-"
                                                                        play sound "punch.ogg"
                                                                        show bryant punch at center
                                                                        m3 "OWW! Stop that!"
                                                                        show bryant normal at center
                                                                        e "Give up the hat, and this will all be over soon, spellslinger."
                                                                        play sound "punch.ogg"
                                                                        show bryant punch at center
                                                                        m3 "OWWowowow. Fine, fine you annoying insect, take it, whatever."
                                                                        hide magicianblue
                                                                        show magician normal at right
                                                                        show bryant normal at center
                                                                        $ hat += 1
                                                                        e "Yes! Only two more to go! Thank you, brute force!"
                                                                        m3 "Hmph. Disgusting creature, *Chomp, slurp, gobble*"
                                                                        e "You’re staying here, I assume, but where are your other friends?"
                                                                        m3 "I’m not sure, I stayed here to sample these delicacies and the others went their own way. The one in the yellow hat frequents that one place with those militant thugs. That’s where I would search for him."
                                                                        e "Wait, you don’t know the other's names either?"
                                                                        m3 "It never came up, really, so it doesn’t matter."
                                                                        m3 "For your information, I’ll be leaving this place as well, as much as I hate to part with these wonderful delicacies."
                                                                        e "What, you finally learned that your force field isn’t impenetrable, so you’re running away?"
                                                                        m3 "..."
                                                                        m3 "... nooo..."
                                                                        m3 "...*Chomp*"
                                                                        e "Whatever. As long as I know the other hats are around here somewhere, I still have a chance to save myself before the lethal curse activates!"
                                                                        m3 "Yeah, you go do that. *burp*"
                                                                        scene bg burgerstore
                                                                        show bryant normal at offscreenleft
                                                                        show burgerdude normal at right
                                                                        show bryant normal at left with move
                                                                        e "I talked with him, and he said he was leaving soon."
                                                                        b "Good. The less people I have to interact with around here, the better."
                                                                        b "..."
                                                                        b "Have a good night, “sir”."
                                                                        jump apartmentn
                                                                elif success == 0:
                                                                    e "Aww, it threw me back here."
                                                                    m3 "You weren’t fast enough, mortal. Completely expected."
                                                                    m3 "This is a labyrinth set to the difficulty of wizards."
                                                                    m3 "It's obvious a mortal would have no chance getting past it."
                                                                    e "Wouldn’t a wizard just teleport to the end?"
                                                                    m3 "... That’s actually the challenge."
                                                                    m3 "..."
                                                                    m3 "... *Chomp*"
                                                                    jump playpenchoices3
                                                                else:
                                                                    e "Nobody likes a quitter..."
                                                                    $ renpy.quit()
                                                label choice20_ask:
                                                    e "So what does eating a shit-ton of burgers have to do with wizardry again?"
                                                    m3 "*Nibble, munch* Foolish mortal... Trying to mock me... "
                                                    m3 "Puppeteering encompasses everything to do on the mortal planes, to some lesser or greater extent, and the desire for exquisite sustenance is no exception. "
                                                    m3 "We’ve had to fast for days while chanting complex spells, and even then only had elixirs and magic beans to survive on after."
                                                    m3 "But this holy mineral you call “Hamburgers” is a culinary breakthrough that earns you the slightest respect in my eyes. Feel honored, mortal."
                                                    e "What, finally realized you prefer eating burgers to playing with dolls?"
                                                    m3 "... I'm getting there. *Chomp*"
                                                    jump playpenchoice
                                                label choice20_psychology:
                                                    e "Ugh... What a pathetic wizard."
                                                    m3 "*Gobble, slurp*"
                                                    e "Your friend back at the police station realized he made a mistake, and was willing to throw away his pride and do the right thing."
                                                    m3 "*Chew, crunch, smack*"
                                                    e "Um... I guess he didn’t really throw away his pride..."
                                                    e "He knew he was doing the right thing by giving me his hat, so he actually felt better as a person AND a magician after the whole thing."
                                                    e "... Besides, the hat looks bad on you anyway. Blue isn’t really your color, doesn’t go with your wizard robes at all. A natural hatless look would suit you better."
                                                    m3 "*Bite, crunch, slurp*"
                                                    e "Oh come on, you can’t “slurp” a burger, you’re not even trying."
                                                    m3 "Shhh... I’m trying to remember how to cast silencing spells."
                                                    jump playpenchoice
                                                label choice20_punch:
                                                    e "Let's try some ”punch in the face” diplomacy, then."
                                                    show forcefield normal at right
                                                    show bryant punch at left
                                                    play sound "punch.ogg"
                                                    e "OW, that shocked me!"
                                                    show bryant normal at left
                                                    m3 "*Chomp* Yeah... Forcefields tend to do that."
                                                    e "Well turn it off so I can punch you in the face."
                                                    m3 "..."
                                                    m3 "NO."
                                                    jump playpenchoice
                                                    
                                                    
            
            
    
    
                                                            
                                                               
                                                            
                                                        
                                                    
                

                                                    
                                                
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                            
                                        
                                            
                                            
                                    jump map
                                elif result == "cemetary":
                                    stop music
                                    play music "scary_music.ogg"
                                    scene bg graveyardday
                                    show bryant normal at left
                                    if (hat == 3):
                                        e "(It’s the cemetery. Yellow hat said the last guy would be here.)"
                                        play sound "spell.ogg"
                                        e "(Eh? What’s that sound?)"
                                        e "(Must be some sort of spell or something, I don’t know.)"
                                        e "(Nowhere else to go but forward, then)"
                                        label cemetarychoiceh3_:
                                            menu:
                                                "Head towards the noise ":
                                                    jump choice26_crypt
                                                "Sing louder than the noise ":
                                                    jump choice26_loud
                                                "Tell the noise to shut up ":
                                                    jump choice26_shutup
                                                "Run away":
                                                    e "(Or, maybe I need to do something else first, I guess)"
                                                    stop music
                                                    play music "main.ogg"
                                                    jump map
                                            label choice26_loud:
                                                e "(THE WHEELS ON THE BUS GO ROUND AND ROUND)"
                                                e "...."
                                                e "AND SHES BUUUUYYYYING A STAIRWAY, TO HEAVEN."
                                                e "..."
                                                e "OPPA GANGNAM STYLE !! Wait, what are the rest of the lyrics?"
                                                e "...."
                                                e "(Whatever the hell I was trying to do just now obviously isn’t working)"
                                                jump cemetarychoiceh3_
                                            label choice26_shutup:
                                                e "HEY! KEEP IT DOWN! SOME OF US ARE TRYING TO SLEEP!!!"
                                                e "YEAH, SLEEP NOW, AROUND THE MIDDLE OF THE DAY."
                                                e "I KNOW IT SOUNDS STRANGE, BUT YOU PROBABLY SHOULDN’T HAVE THE VOLUME UP SO HIGH ANYWAYS."
                                                e "..."
                                                e "I guess they can’t hear me, or they just don’t care."
                                                jump cemetarychoiceh3_
                                            label choice26_crypt:
                                                e "(The sounds are all coming from...)"
                                                e "(This room?)"
                                                scene bg crypt
                                                show magicianred normal at right
                                                show bryant normal at left
                                                m "Oh? Yes, hello mortal, nice of you to join me."
                                                m "Not really. Wipe your feet before coming in, too."
                                                e "Oh, sure, sorry. And what’s with the music?"
                                                m "Ancient incantations far beyond the scope of your relatively limited comprehension, or likely anyone overly familiar with this plane of existence. Calling it “music” is a misnomer."
                                                e "Yeah, yeah, I’ve heard enough magic nerd shit for a life time"
                                                e "Speaking of which, hand over the hat so I can break this curse already"
                                                m "I’m afraid I won’t be swayed as easily as my brethren, mortal."
                                                e "What? Are you the omnipotent wizard demon I have to have an epic duel with now?"
                                                m "No, even worse. I’m the only one actually aware of the curse on you!"
                                                e "Eh? They knew about it, I even reminded them about the lethal part."
                                                m "Yes, but need I remind YOU what we all deemed the “lethal part”?"
                                                e "Uh, a “minor” side effect?"
                                                m "Exactly. The curse of the puppet"
                                                m "one of the few ways for a living being to feel like a puppet, with someone else controlling the strings."
                                                m "Imagine: a stranger with no emotional or physical ties to you is suddenly granted control over your every move with no threat of retribution."
                                                m "Imagine the atrocities they would have you commit, the unspeakable acts they could force you to do for nothing else than their own petty amusement."
                                                m "Every second there is a risk of some new erratic action."
                                                m "Every day there is a chance that they break you out of mere boredom, until you realize the rest of your pathetic, meaningless life is never going to be lived out the way you wanted."
                                                m "But you don’t have to imagine, do you?"
                                                m "You’ve experienced it yourself, the feeling of helpless, abject terror of not being in control of your own actions."
                                                m "I feel that you’re no different than when we first met."
                                                m "The curse, besides the unintentional lethality, was meant to teach you what it’s like, the mere basest of feelings, to have someone else pulling the strings."
                                                m "It should make you feel at your very core, the awe inspiring connection between puppet and puppeteer that we strive among all else to comprehend."
                                                m "I am guessing that you haven’t learned shit, have you mortal?"
                                                e "Whoa, well, I mean um, when you put it that way…"
                                                e "At first I just wanted to get rid of the puppeteer part. Does that count?"
                                                m "I thought not. I KNEW not."
                                                m "Which is why, mortal, I offer you my hat."
                                                e "…What?"
                                                m "Yes, come take it. Consider it your final test"
                                                m "the others had their own for you, in various forms, correct?"
                                                e "..."
                                                m "But on your way, be sure not to step on that pressure plate to your right!"
                                                e "Eh?"
                                                m "Yes, that one. It’s linked to an explosive rune that would certainly be lethal for whomever stepped on it."
                                                m "Pay it no heed, mortal. Just step over here."
                                                menu:
                                                    "Step on the trap":
                                                        e "You mean THIS pressure pla-"
                                                        play sound "explosion.ogg"
                                                        hide bryant
                                                        show explosion normal at left
                                                        m "“…Yes, that one"
                                                        m "I guess it doesn’t matter so much that he didn’t wipe his feet, now."
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done
                                                    "Step towards him ":
                                                        m "That’s right, this way."
                                                        m "But not over there"
                                                        m "those are where I keep the Stradyl samples."
                                                        m "They are poisonous mushrooms, causing whoever eats them to reveal their darkest, innermost and most likely embarrassing secret before dying from explosive diarrhea."
                                                        m "But you don’t care about those, do you?"
                                                        menu:
                                                            "Eat the mushrooms":
                                                                e "Using reverse psychology, eh? Ha, I’ll eat them all at once!"
                                                                "*Bryant Runs over and eats a few at once*"
                                                                e "I THINK MY MOM IS HOT, AND I STILL PISS MY BED SOMETIMES!"
                                                                e "WAIT, WHAT THE FUCK, OH MY GOD, I HAVE TO SHIT REAL BAD! AGHHHHH!"
                                                                e "“SHIT, SHIT, SHIT!!! LITERALLY, SHIIIITTTT! AAAAAHHH!!!"
                                                                e "BY THE WAY, I REALLY LIKE BOY BANDS AND I THINK MOST OF THE SINGERS ARE KINDA CUTE BUT I’M NOT GAY… I THINK…"
                                                                e "AAHHHHHHHHHHH!!!"
                                                                m "-...I should have thought that one through."
                                                                scene bg death
                                                                stop music
                                                                play music "scary_music.ogg"
                                                                pause
                                                                jump choice0_done
                                                            "Keep walking":
                                                                e "Um, err, no thanks"
                                                                m "On a one track mind today, aren’t we, mortal?"
                                                                m "I suppose I can’t distract you with that pile of currency next to the collection fairly lethal shock rune?"
                                                                menu:
                                                                    "Go get the money":
                                                                        e "Well, free money can’t be that bad, I suppose."
                                                                        e "Wow, this is actually a lot-"
                                                                        e "OWOWOWOW HOW UNEXPECTED OWOWOW!"
                                                                        scene bg death
                                                                        pause
                                                                        jump choice0_done
                                                                    "Keep walking":
                                                                        e "Hey, quit pointing out all the lethal things in the room as I walk towards you."
                                                                        m "But then how else would you know about the trapdoor that leads to a pit of man eating parakeets underneath that rug there?"
                                                                        menu:
                                                                            "Check under the rug":
                                                                                e "Man eating parakeets? Yeah right, probably man tickling at worst"
                                                                                hide bryant
                                                                                e "C’mon out, little birdies. Actually, I’ve always wanted a pet-"
                                                                                e "OW! That hurts, knock it off! HEY, NO! NO! AAARRRGGGHHH!"
                                                                                e "*burp*"
                                                                                m "(...I knew there was a reason to keep those things around.)"
                                                                                scene bg death
                                                                                stop music
                                                                                play music "scary_music.ogg"
                                                                                pause
                                                                                jump choice0_done
                                                                            "Keep walking":
                                                                                e "Enough! I’m obviously just going to keep walking, now just hold tight"
                                                                                m "Keep walking, eh? Even if I conjure a rebounding force field in front of me?"
                                                                                show forcefield normal at right
                                                                                menu:
                                                                                    "Go around it ":
                                                                                        e "So I’ll just walk around it, I have common sense."
                                                                                        hide forcefield normal
                                                                                        m "Do you?"
                                                                                        m "Or do you realize now that maybe someone else does too?"
                                                                                        m "Maybe it’s something different than common sense"
                                                                                        m "sympathy."
                                                                                        m "Someone who doesn’t know you personally, who wouldn’t lose anything from your death or injury, decided to help you pass the challenges and avoid a thousand terrible fates."
                                                                                        m "He helped you discover the clues, pass the challenges, uncover secrets, and defeat remarkable wizards."
                                                                                        m "For what?"
                                                                                        m "Do you think he gets something for breaking the curse?"
                                                                                        m "Some prize or reward"
                                                                                        m "a medal of honor?"
                                                                                        m "Was it for his own amusement?"
                                                                                        m "Is he just that bored?"
                                                                                        m "Or perhaps some people prefer Naches, rather than Schadenfreude?"
                                                                                        m "Yes, someone put their thoughts and feeling through your eyes."
                                                                                        m "They imagined what they would have felt for you, even though you’re nothing more than a doll to them."
                                                                                        m "Empathy and sympathy, one of the greatest advancements humanity can ever achieve"
                                                                                        m "those things brought you here, before me."
                                                                                        m "I think you’ve learned something too" 
                                                                                        m "perhaps unconsciously, perhaps forced, perhaps innate in your very being."
                                                                                        m "Trust."
                                                                                        m "You trusted your puppeteer to do the right thing."
                                                                                        m "You knew he could."
                                                                                        m "And he didn’t let you down, with nothing going for him but your hopes and dreams on the line."
                                                                                        m "This is what the curse is meant to teach, and this is what I believe you have finally learned."
                                                                                        m "I humbly offer you my hat, and with it, your life."
                                                                                        menu:
                                                                                            "Ask about the blatant plot holes":
                                                                                                e "..."
                                                                                                m "..."
                                                                                                e "What the fuck is that load of shit?"
                                                                                                m "Eh?"
                                                                                                e "All your friends, except the red one maybe, seemed to not give a shit if I learned anything or not."
                                                                                                e "Actually, the yellow one flat out tried to kill me."
                                                                                                e "Uh…well…"
                                                                                                e "And how can you act like this was all some stupid learning experience?"
                                                                                                e "It was going to kill me after %(difficulty)d days, and you probably wouldn’t even remember if it wasn’t for me coming over here to remind you, right?"
                                                                                                e "And this whole thing started when he made me do all that weird stuff on the first day, right?"
                                                                                                e "How is that trust building?"
                                                                                                m "NO…um…uh…"
                                                                                                e "What’s the point of making me learn, anyways?"
                                                                                                e "Do YOU get a medal or something, huh? What?"
                                                                                                m "Well, I mean, it’s more…uh…"
                                                                                                e "Not that you probably thought that far ahead, right?"
                                                                                                e "All those lethal traps you were pointing out was probably just you hoping whoever was controlling me would ram me into them, right?"
                                                                                                m "Hey…there’s no, proof…umm…"
                                                                                                e "How are you casting all this shit, anyways?"
                                                                                                e "How has no one found out about all this voodoo magic when you’re screaming your heads off about dolls and casting force fields all over the place?"
                                                                                                m "Actually, there’s a very logical explanation-"
                                                                                                e "That involves more “deus ex machine” magic, right?"
                                                                                                e "What the fuck do half your spells have to do with Puppeteering, anyways?"
                                                                                                e "Unless puppets have something to do with force fields that I’m currently unaware of."
                                                                                                e "How did you learn that crap anyways?"
                                                                                                e "Is there some science behind it?"
                                                                                                e "How do you just arbitrarily give control of my actions to some unknown force possibly a thousand miles away just by chanting?"
                                                                                                e "What’s up with your friends anyways?"
                                                                                                e "Is magic inversely proportional to common sense or something?"
                                                                                                e "You apparently have infinite magical powers but you go about your day cursing retailers and stealing burgers?!"
                                                                                                e "Also, did you curse all the cops in the city or something?"
                                                                                                e "They each have their own personal emotional problems that apparently hinder their cognitive skills."
                                                                                                e "Most serious crimes are only worth half a day in jail, where they conveniently release me with just enough time to go home."
                                                                                                e "What if the unknown force had “save files” or something?"
                                                                                                e "Couldn’t they just be throwing me into every possible danger for their own sadistic amusement then reloading till they got the ending right with sheer luck?"
                                                                                                m "Now you’re just making things up-"
                                                                                                e "THIS WHOLE FUKING PLOT IS MADE UP, AHH!!!"
                                                                                                m "Chill, mortal."
                                                                                                e "Why do you call everyone mortal?"
                                                                                                e "Are the magicians immortal or something?"
                                                                                                e "Puppeteers I mean?"
                                                                                                e "Why do you call yourselves puppeteers if I never see anything puppet related come out from you-"
                                                                                                m "FINE, GEEZ, NOTHING MAKES SENSE, OK? YOU WIN!"
                                                                                                m "Now just take my hat and be happy the curse is gone."
                                                                                                hide magicianred
                                                                                                show magician normal at right
                                                                                                e "How does just having the hats break the curse?"
                                                                                                e "Didn’t you chant something to curse me?"
                                                                                                e "Shouldn’t there be a “counter-curse” or something more complicated than just having your 4 hats with me?"
                                                                                                e "And what’s with your hats?"
                                                                                                e "Do you lose your power when they’re gone or something?"
                                                                                                e "Why else would it be important to collect them if-"
                                                                                                m "Urg, fuck this shit. I’m out."
                                                                                                e "OUT?!?!"
                                                                                                e "HOW?!?"
                                                                                                e "DOES TELEPORTING NOT NEED TO BE CHANTED OR SOMETHING?"
                                                                                                e "CAN’T YOU CURE WORLD HUNGER OR SOMETHING WITH ALL THAT POWER?"
                                                                                                m "Magic, bitch, I don’t have to explain shit. Peace out."
                                                                                                play sound "spell.ogg"
                                                                                                hide magician
                                                                                                e "NOOOOO"
                                                                                                e "How am I going to live with all these obvious inconsistencies in my world, now?"
                                                                                                e "Am I just going to ignore the fact there’s some crazy magic bastard with no common sense just wandering around?"
                                                                                                e "And what am I going to do with all this lethal stuff he just left behind?"
                                                                                                e "..."
                                                                                                e "Oh, that’s right, those options aren’t coming up anymore."
                                                                                                e "I’m free!!!"
                                                                                                jump cryptlast
                                                                                            "Punch him in his stupid, psychotic little weirdo face ":
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OW! What the hell, mortal?"
                                                                                                e "What the hell?"
                                                                                                e "WHAT THE HELL?"
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OWWW!"
                                                                                                e "You, and your weirdo fucking friends."
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OWWW, STOP IT"
                                                                                                e "Dump some lethal brainwashing shit on me…"
                                                                                                e "You make me run around town for days solving your stupid shitty puzzles…"
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OWCH, KNOCK IT OFF!"
                                                                                                e "You tried to kill me off multiple times, and to tell me I fucking deserve it…"
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OOWWWW!!!"
                                                                                                e "AND YOU THINK I’M JUST GONNA DROP ALL THAT IF YOU TELL ME SOME SOB STORY ABOUT LEARNING TO TRUST THE FUCKING PSYCOPATH WHOSE BEEN MAKING ME DO ALL THIS WEIRD SHIT IN THE FIRST PLACE?!?!?”"
                                                                                                e "OW, FUCKING FORCE FIELD, OW!"
                                                                                                show forcefield normal at right 
                                                                                                e "WHOA!"
                                                                                                m "FINE, WHATEVER, GEEZ, JUST TAKE THE FUCKING HAT!"
                                                                                                e "DON’T GIVE A FUCK IF YOU LEARNED ANYTHING NOW!"
                                                                                                hide magicianred
                                                                                                show magician normal at right
                                                                                                m "BIBBIDY BOBBIDY BOO!"
                                                                                                m "CURSE UNDO AND SHIT!"
                                                                                                m "Good day!"
                                                                                                m "TELEPORTING OUT!"
                                                                                                m "FUUUCK"
                                                                                                play sound "spell.ogg"
                                                                                                hide magician
                                                                                                e "Well shit, what am I going to do with all these hats, now?"
                                                                                                e "Wait, that’s right, I’m free!"
                                                                                                jump cryptlast
                                                                                            "Just roll with it for the corny ending, already ":
                                                                                                e "..."
                                                                                                e "You’re right, you are completely right."
                                                                                                e "All this time, he’s actually been helping me along."
                                                                                                e "I guess I just unconsciously just felt normal, you know?"
                                                                                                e "He knew what I had to do, and helped me achieve my goal."
                                                                                                e "Even back at that nightclub, he helped me dodge bullets, I mean-"
                                                                                                m "The puppet often feels like it can do more than it ever could, when the puppeteer brings it down from the shelf."
                                                                                                m "And with your experiences in tow, you now have the chance to be the puppeteer of your own life."
                                                                                                hide magicianred
                                                                                                show magician normal at right
                                                                                                m "With the hats in your possession the curse is undone entirely."
                                                                                                m "Your actions are now forever your own."
                                                                                                m "You can go back to your “average life” back in that bookstore…"
                                                                                                m "But after that amazing performance,"
                                                                                                m "Who could be content with such a repetitive act, eh?"
                                                                                                m "my brethren and I will bother you no more."
                                                                                                m "We were planning to go back to Florida soon."
                                                                                                m "There are a lot more people like us there"
                                                                                                e "You mean complete weirdoes or magicians?"
                                                                                                m "Only weirdoes, but we could use the company sometimes."
                                                                                                m "Farewell, Bryant Day."
                                                                                                hide magician 
                                                                                                play sound "spell.ogg"
                                                                                                e "Whoa, he teleported out."
                                                                                                e "…Well, now what should I do?"
                                                                                                e " ... "
                                                                                                e "…Oh, wait, that’s right."
                                                                                                e " I'm free!"
                                                                                                jump cryptlast
                                                                                                
                                                                                                label cryptlast:
                                                                                                        stop music
                                                                                                        play music "main.ogg"
                                                                                                        scene bg graveyardnight
                                                                                                        show bryant normal at center
                                                                                                        e "Well, now that that’s all over with, life can finally return to normal."
                                                                                                        scene bg burgerstore
                                                                                                        show bryant normal at left
                                                                                                        e "But how have things changed?"
                                                                                                        e "Hmmm…"
                                                                                                        e "Well I’m still alive, aren’t I?"
                                                                                                        e "And I guess I still have my job to return to ..."
                                                                                                        scene bg citysidewalk
                                                                                                        show bryant normal at left
                                                                                                        if (hobo < 2):
                                                                                                            show hobo normal at right
                                                                                                            e "Hmmm, I don’t think I’m in trouble with the law anymore…"
                                                                                                            h "Hey, gimmie some cash, kid."
                                                                                                            e "Not in the mood, hobo."
                                                                                                            h "Piss off then, you arrogant little terd! *mumble mumble*"
                                                                                                        else:
                                                                                                            e "Hmmm, I don’t think I’m in trouble with the law anymore…"
                                                                                                            e "..."
                                                                                                            if(hobo == 2):
                                                                                                                e "Oh that’s right... The hobo left..."
                                                                                                                e "Another thing to look forward to."
                                                                                                            else:
                                                                                                                e "Oh that's right... I assassinated lord hobo..."
                                                                                                                e "Still don't know how I feel about that..."
                                                                                                        scene bg alley
                                                                                                        show bryant normal at right
                                                                                                        if (bank == 0):
                                                                                                            e "Oh, that’s right!"
                                                                                                            e "I spent all my saving didn’t I…"
                                                                                                            e "..."
                                                                                                            e "Okay, so that’s a problem…"
                                                                                                        else:
                                                                                                            "I’ve still got some money saved up in the bank, I can pay off any debts I owe…"
                                                                                                        scene bg apartmentday
                                                                                                        show bryant normal at center
                                                                                                        e "Overall, I guess things turned out pretty ok."
                                                                                                        e "I can go back to work tomorrow, and no one will ever realize what happened."
                                                                                                        e "I can be perfectly average again."
                                                                                                        e " Well, maybe it WOULD get a little boring being average ALL the time…"
                                                                                                        e "… And that puppeteer…"
                                                                                                        e "I guess he wasn’t really such a bad dude, after all."
                                                                                                        if (evedate == 1):
                                                                                                            e "Oh wait, there’s a message on my phone from eve."
                                                                                                            e "Oh wait, that’s right!"
                                                                                                            e "We’re dating now!!!"
                                                                                                            e "..."
                                                                                                            e "You really weren’t a bad guy at all, were you, my puppeteer wingman?"
                                                                                                        if (evedate == 1) and (hobo == 3) and (assasin == 1):
                                                                                                            e "Wait, another message?"
                                                                                                            e "…and who is this from?"
                                                                                                            e "…Al Capone?"
                                                                                                            e "…oh, right, the hobo is gone, so…"
                                                                                                            e "... I guess I’m an assassin as well…"
                                                                                                        elif (hobo == 3) and (assassin == 1):
                                                                                                            e "…wait, what’s this message on my phone?"
                                                                                                            e "…It’s from…"
                                                                                                            e "…Al Capone?"
                                                                                                            e "…oh, right, the hobo is gone, so…"
                                                                                                            e "... I guess I’m an assassin as well…"
                                                                                                        scene bg title with fade
                                                                                                        pause
                                                                                                        scene bg credit with fade
                                                                                                        pause
                                                                                                        scene bg credit2 with fade
                                                                                                        pause
                                                                                                        jump choice0_done
                                                                                                   
                                                                                        
                                                                                        
                                                                                    "Keep walking":
                                                                                        e "Well, I can’t just stop halfway, right? That’d be like giving u-"
                                                                                        e "WOAAA!!!"
                                                                                        m "(Oh, snapped his neck.)"
                                                                                        m "(…Perhaps I should have mentioned how strong the rebounding effect was…)"
                                                                                        m "(…Eh, he should have guessed it himself by now.)"
                                                                                        scene bg death
                                                                                        stop music
                                                                                        play music "scary_music.ogg"
                                                                                        pause
                                                                                        jump choice0_done
                                    else:
                                        e "It’s the cemetery"
                                        e "no one I know is dead yet, so there’s no real-"
                                        e "*AUUGG*…What’s that sound?"
                                        play sound "spell.ogg"
                                        e "Urgh…it’s making…me…ugh…"
                                        e "This…is bad..."
                                        label cemetarychoice:
                                            menu:
                                                "Head towards the noise":
                                                    jump choice26_cryptb
                                                "Sing louder than the noise":
                                                    jump choice26_loudb
                                                "Tell the noise to shut up ":
                                                    jump choice26_shutupb
                                                "Run away":
                                                    jump choice26_runb
                                        label choice26_cryptb:
                                                e "(Gah…if I reach the noise…then…maybe…)"
                                                e "(Urg…)"
                                                e "...."
                                                e "Ah…blacking…out…"
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                        label choice26_loudb:
                                                e "MARY HAD A LITTLE… Urgh…"
                                                e "ALL THE SINGLE LADIES…all…the…"
                                                e "Urgh…IT’S THE…EYE OF THE… tiger…"
                                                e "WALK UP…in…the club…like…what up…I got…a…big…err…"
                                                scene bg citysidewalk
                                                show citizen normal at right
                                                c "(What’s with that weird music at the cemetery? It’s been playing like that for a few days.)"
                                                c "(Oh, there goes someone to check. Maybe he’ll make them turn it off)"
                                                c "(Eh? Is he sick or something? He doesn’t look to goo-)"
                                                e "MARY HAD A LITTLE… Urgh…"
                                                e "ALL THE SINGLE LADIES…all…the…"
                                                e "Urgh…IT’S THE…EYE OF THE… tiger…"
                                                e "WALK UP…in…the club…like…what up…I got…a…big…err…"
                                                c "And he collapsed…"
                                                c "I think I’ll just keep walking"
                                                scene bg death
                                                pause
                                                jump choice0_done
                                        label choice26_shutupb:
                                                e "GODDAMMIT, SHUT UP."
                                                "*Music continues to play*"
                                                e "Ugh…"
                                                jump cemetarychoice
                                        label choice26_runb:
                                            e "Urg…got to, get away…"
                                            scene black
                                            "*Hours later*"
                                            scene bg graveyardnight
                                            show bryant normal at left
                                            e "Urg…"
                                            e "Ugh, that music is still going on-"
                                            e "Wait, its night already?!? I must have been passed out for most of the day!"
                                            e "I shouldn’t even bother trying to walk back into it, it’d be suicide for sure."
                                            e "There’s nothing else I can do now"
                                            e "I might as well head back home."
                                            jump apartmentn
                                                
                                    jump map
                                elif result == "sidewalk":
                                    scene bg citysidewalk
                                    show bryant normal at left
                                    if (hobo >= 2):
                                        e "(It’s the sidewalk on my way to work, but beggar free.)"
                                        if(hobo == 3):
                                            e "(I don't know how I feel about having killed him...)"
                                        else:
                                            e "(It was worth the $200.)"
                                        e "(When this curse is all sorted out, I’ll be able to walk to work without someone screaming obscenities at me and demanding small change.)"
                                        e "(Maybe I’ll miss him; he seemed to liven up a bit when I gave him a little.)"
                                        e "..."
                                        e "Nawww..."
                                        jump map
                                    show hobo normal at right    
                                    e "(Nothing special here, though it is on my path to work.)"
                                    e "(Oh, wait, right.)"
                                    e "(The hobo...)"
                                    if (hobo == 0):
                                        h "Ay, you! Yeah, you! Gimmy some cash, you’re just gonna waste it anyway."
                                    else:
                                        h "Oh, its you again. Spare anything else fer a starving beggar?"
                                    label swalkchoice:
                                        menu:
                                            "Ignore him and leave":
                                                h "Yeah, keep walkin sonny. I’ll stay right here, waiting for someone to give a shit."
                                                jump map
                                            "Ask about him ":
                                                jump choice22_ask
                                            "Give him 100$ ":
                                                jump choice22_give
                                            "Punch him":
                                                jump choice22_punch
                                            "Help him get a job ":
                                                jump choice22_job
                                        label choice22_ask:
                                            if (hobo == 0):
                                                e "How’d you end up here anyway? And don’t you ever go anywhere else? To eat or something?"
                                                h "Oh, look at sonny boy here, eh, pretending to care but won’t cough up any cash. What a faker, spoiled bourgeoisie 92 percent something or other grumble grumble."
                                                e "People might jump for a sob story? "
                                                e "Can you make anything up at least?"
                                                h "You calling me a sob? I’ll sob you, you... Damn kids mocking me when I’m down on my luck."
                                                e "Come on, anything about yourself?"
                                                h "I need cash, asshole. Gimmy whatever you got."
                                                jump swalkchoice
                                            else:
                                                e "Whats your story?"
                                                h "Me? Eh, I was always like this. Really. Can’t remember much else."
                                                e "What, you were born begging?"
                                                h "Well, I mean, uhhh... Well, I guess I did... live in... ehh... ummm..."
                                                h "Kinda a large family... erm... eh... not much to... ah... eat..."
                                                h "Oh fuck it, I lived in a mansion."
                                                e "Woa, unexpected. What happened?"
                                                h "Uh... ah... ehhh..."
                                                e "What, were your parents overly flamboyant and arrogant about rich, giving you a complex against those with high social status and causing you to alienate yourself from them in an act of defiance and run away to become a homeless vagabond?"
                                                h "What? Fuck no, I gambled till they threw me out."
                                                e "HA! Knew it."
                                                h "Shut up, you lucky little sob... grumble grumble..."
                                                jump swalkchoice
                                        label choice22_give:
                                            e "Here, have some cash."
                                            if (money == 0):
                                                e "... Uh, actually, it seems I don’t have any money on me."
                                                h "Oh, riiight, I get that all the time, asshole. All you snobs and your fancy coats and your fancy hats with your “Oh, I don’t have any spare money for a starving man”."
                                                h "Well then why don’t I see you sitting down here with me? Huh?"
                                                e "Because we go out to work for money?"
                                                h "... Fuck you."
                                                jump swalkchoice
                                            elif (hobo == 0):
                                                $ money -= 100
                                                $ hobo += 1
                                                h "Now we’re talkin, sonny. This much will keep me steady for weeks."
                                                jump swalkchoice
                                            else:
                                                $ money -= 100
                                                $ hobo = 2
                                                h "Well holy shit. Aren’t you the bees knees."
                                                h "With this much moolah, I don’t need to sit here rotting up the place anymore."
                                                h "I’ve got enough to live out my dreams now. Thanks a lot kid, you’ve given me a brand new faith about this whole “humanity” thing!"
                                                e "You know, it's entirely possible for you to work for that money yourself."
                                                h "Don’t push your luck, kid."
                                                h "I’m off for adventure. Good luck with whatever shit you’re doing, I guess."
                                                show hobo happy at offscreenright with move
                                                e "(Well, at least in the end, he finally learned to say thank you.)"
                                                e "(In a way, I guess.)"
                                                e "(And, actually, it did kinda cost 200$ overall...)"
                                                e "..."
                                                e "(Hobo's gone. Worth it.)"
                                                e "(Now, back to the curse...)"
                                                jump map
                                        label choice22_punch:
                                            e "Want some food instead?"
                                            h "Eh?"
                                            e "How’s about a knuckle sandwich?"
                                            show policeman normal at offscreenright
                                            show policeman normal at center with move
                                            p "Hold it right there, bub."
                                            e "Wait, what?!? Where did you come from?"
                                            p "I’ve been here the whole time. The city’s got a special division posted just for defending this hobo."
                                            h "Oh, shit! Get him, officer! Blow his fucking brains out!"
                                            e "You’re telling me the city has an entire police division just for defending this annoying prick?"
                                            h "Officer! He’s crazy, I tell ya! Went feral right in front of me, he did!"
                                            p "Think about it: in every successful city, you always think of hobos panhandling on the street, right?"
                                            p "This guy here’s the last homeless man in the city."
                                            p "If we lose him, it's like we’re losing part of the qualification."
                                            h "You tell him, officer! Beat the shit outta him!"
                                            e "So you have an entire division defending him just because his social status makes your workplace more diverse? I should sue for discrimination!"
                                            p "Doesn’t matter why we’re defending him, bub; I caught you red handed about to lay hands on this beggar."
                                            h "Hey, officer? Can I get his wallet?"
                                            e "So what’s the punishment then?"
                                            p "You’ll be-"
                                            h "Hey officer! His walle-"
                                            p "FOR FUCK'S SAKE, SHUT UP."
                                            h "..."
                                            p "..."
                                            p "Jesus, I gotta hear you beg all day, but I ain’t tolerating this shit."
                                            e "...so my punishment?"
                                            p "... Well, I guess I can’t really blame you for wanting to beat the shit outta him... How’s about I just hold you at the station for a while and let you go at sunset?"
                                            e "Fine with me."
                                            h "... Pig cops, conspiring against me with rich snobs, grumble grumble."
                                            scene black
                                            "*hours later*"
                                            jump apartmentn
                                        label choice22_job:
                                            e "Why don’t you get a job?"
                                            h "They think they’re too good for me... Well I’m too good for them. They just don’t know it, I’ll have you know."
                                            e "Why don’t you let them know instead?"
                                            e "Look, I can see a help-wanted poster across the street. Just ask for some work there."
                                            h "Da-fucks your problem, boy? Don’t butt in on other people’s business. Look at you, mocking a poor beggar."
                                            e "But you were just asking me for money a second ago."
                                            h "Now what, you’re bragging about it?"
                                            h "Probably some rich snot with nothing better to do than annoy me, rather than helping me with some cash, eh, aren’t you? Feels good, rich boy? Having fun?"
                                            e "(Ugh... This isn’t working at all.)"
                                            jump swalkchoice
                                        

                                               
                                                
                                                
                                                
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                    
                                    
                                        
                                    jump map
                                elif result == "statue":
                                    if (statuedestroyed == 2):
                                        jump statue6
                                    elif (statuedestroyed == 3):
                                        jump statue9
                                    elif (statuedestroyed == 1):
                                        scene bg citystatue
                                        show bryant normal at left
                                        e "Here’s the town statue, made in the image of our apparently very vain mayor."
                                    else:
                                        scene bg citystatue
                                        show bryant normal at left
                                        e "Here’s the town statue, made in remembrance of some famous dead guy I don’t know."
                                        e "Nothing to do here."
                                        e "There’s not even anyone around."
                                        label statuechoice:
                                        menu:
                                            "Leave":
                                                e "Right then, back to questing."
                                                jump map
                                            "Read about the statue":
                                                jump choice13_read
                                            "Vandalize the statue":
                                                jump choice13_vandalize
                                        label choice13_read:
                                            #$ statuedestroyed == 1
                                            e "Let's see, says here..."
                                            e "... Famous dead guy... is actually the mayor. Guess he’s still living, actually..."
                                            e "Wait, that means I had no idea what the mayor looked like until now."
                                            e "Well then, I guess that means it didn’t matter until now."
                                            e "Learn something new every day when mystical unknown forces control your every move, I suppose."
                                            jump statuechoice
                                        label choice13_vandalize:
                                            e "Vandalize public property, why not."
                                            $ statuedestroyed = 2
                                            scene black
                                            "*Hours later*"
                                            scene bg citystatuedestroyed
                                            show bryant normal at left
                                            e "After hours of hard work and dedication, I’ve reduced a monument in someone’s honor to a ugly looking scrap heap. I don’t think I’m liking this curse shit at all..."
                                            show policeman angry at offscreenright with move
                                            show policeman angry at right with move
                                            p "Hold it right there, scumbag."
                                            e "Oh, shit! It's the fuzz!"
                                            e "Actually I’ve been vandalizing a public statue in the middle of a street for a few hours now. Why am I surprised the police showed up?"
                                            e "Actually, its kinda strange it took them so long to notice. It took me a good hour or two to rip off the head, and I was on top of it prying the whole time."
                                            p "That’s enough of your derogatory monologue. You’re under arrest for vandalism, buddy!"
                                            menu:
                                                "Give up":
                                                    e "I give up, take me away."
                                                    p "Not gonna try and run away? Good."
                                                    label statuevchoice:
                                                        p "Normally vandalism of this scale would get you sent away for a year or two, but the mayor said it was his statue, and he doesn’t mind."
                                                        e "Oh, wow. This mayor sounds like a real nice guy."
                                                        e "Makes me kinda feel bad for vandalizing a statue of him for the past couple hours."
                                                        p "Yeah, well feel bad about it for a few hours more. We’re still locking you up for the rest of the day, so don’t get too smug."
                                                        e  "Don’t worry, I won’t."
                                                        scene black
                                                        "*Hours later*"
                                                        jump apartmentn
                                                "Run for it ":
                                                    e "Uh, look over there, a dog with a curly tail!"
                                                    p "Oh? Where? You mean behind the massive vandalized statue?"
                                                    show bryant normal at left with move
                                                    show bryant normal at offscreenleft with move
                                                    p "I don’t see- ohhh, I get it."
                                                    p "There wasn’t any dog at all. I was fooled."
                                                    p "Clever move, mystery vandal, very clever indeed."
                                                    jump map
                                                "Duke it out with him ":
                                                    e "Hows about I smack you one in the gob and make off into the sunset scot free instead, “buddy”, eh? Whatdayathink of that?"
                                                    p "I think I have a gun."
                                                    e "Oh."
                                                    e "Right..."
                                                    e "I keep forgetting these simple thi-"
                                                    show policeman shooting at right
                                                    pause
                                                    scene bg death
                                                    stop music
                                                    play music "scary_music.ogg"
                                                    pause
                                                    jump choice0_done
                                    label statue6:
                                        scene bg citystatuedestroyed
                                        show bryant normal at left
                                        e "Here’s the town statue. That I vandalized. Hm."
                                        e "Nothing to do here."
                                        e "There’s not even-"
                                        e "Loljk there’s a cop right behind me..."
                                        show policeman normal at right
                                        p "Excuse me sir, do you happen to know anything about what occurred here?"
                                        p "Actually, you look kinda familiar ..."
                                        menu:
                                            "Admit it":
                                                e "Oh, yeah, um, this was kinda my fault."
                                                p "I knew it! The perpetrator always returns to the scene of the crime!"
                                                p "And there are no dogs with curly tails in a 10 mile radius, I checked, so you can’t fool your way out of this one!"
                                                jump statuevchoice
                                            "Deny it ":
                                                e "Uh, no, no idea, what, does this place not normally look like this?"
                                                p " ..."
                                                p "Eh, no, it doesn’t. We’re still looking for the vandal who did it."
                                                p "He looks exactly like you, though. So if you see anyone who looks exactly like you in every way, bring him in for questioning please."
                                                e "Uh, sure thing officer."
                                                e "What is with all the cops around here? If I knew they were this stupid before this whole curse thing, I’d forget the whole average business and just go around robbing banks in broad daylight."
                                                e "Doesn’t matter, I guess. At least I’m off the hook for now."
                                                jump map
                                            "Punch him in the face":
                                                p "Does THIS look familiar?"
                                                p "Oh no! He’s armed with an arm! And he’s running straight for my face from 10 feet away!"
                                                p "Good thing I’m a cop with a gun and the right to defend myself."
                                                show policeman shooting at right
                                                e "Oh, right, that."
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                    label statue9:
                                        e "There’s the statue I vandalized..."
                                        e "Hm, its been a day or two but they still haven’t picked up the place at all."
                                        e "Was I suppose to clean it up for community service or something? All they did was lock me in a cell for most of the day and told me I was free to go back home..."
                                        e "Maybe they’re leaving it for other criminals to clean up for THEIR sentences or something?"
                                        e "Or maybe they like what I did with it. It kinda looks like modern art, sorta."
                                        e "Not very average, like it was before, but for statues average means ugly and ignorable, so its kind of an improvement."
                                        e "The graffiti was actually a nice touch. They really should have paid me instead of arresting me."
                                        e "..."
                                        e "Now that I think about it, I can’t believe I just said that."
                                        e "I am turning more and more unaverage by the day, aren’t I?"
                                        e "Ugh, gotta hurry up and find a cure for this curse."
                                        jump map
                                                
                                                
                                    jump map
                                elif result == "nightclub":
                                            scene bg nightclub
                                            show bryant normal at offscreenleft
                                            show gangster normal at center
                                            show gangster2 normal at right
                                            show bryant normal at left with move
                                            
                                            #if (nightclubdone):
                                            #    "Nothing to do here."
                                            #    jump map
                                            
                                            e "Oh geez, this has to be the shadiest place I’ve ever unwillingly visited in my entire average life."
                                            g "Hey, what do you want?"
                                            
                                            label nightclubmenu1:
                                                menu:
                                                    "Leave":
                                                        e "Uh, umm, I’ll just be leaving..."
                                                        g "Right on, brutha. Peace, dawg."
                                                        jump map
                                                    "Ask for drugs":
                                                        jump nightclub_2
                                                    "Repremand them":
                                                        jump nightclub_3
                                                    "Ask to talk to their boss":
                                                        jump nightclub_4
                                                    "Pretend to be a cop":
                                                        jump nightclub_6
                                                    
                                            label nightclub_2:
                                                e "Hey, uh, you got any drugs?"
                                                g "Woa, dog, drugs ain’t cool."

                                                g2 "Yeah man, Don’t they burn your brain and shit? Unhealthy shit, man."

                                                e "Oh, right. Sorry for asking."

                                                g "Treatin us like a coupla dealers, fool. No respect."
                                                jump nightclubmenu1
                                                
                                            label nightclub_3:
                                                e "Look at yourselves. Can’t you think of anything better to do than play “gangster” and cause suffering for your own selfish gain?"

                                                g "Whoa, dog, don’t you be judging us."

                                                g2 "Yeah, man, I gotta get some money for my momma’s operation, or she’s wasted bro!"

                                                g "And my sister, dude, she’s coughin' and weezin' up a storm back home."
                                                g2 "You sayin' that we should sit tight while our family’s at death's door bro?! You sayin' you wouldn’t man up and do whatever you needed to do for yo family? Huh?!"

                                                e "Oh, geez, I didn’t know...Sorry."

                                                g2 "Ha, we're just messin with you fool.It's all for the cash."

                                                g "Yeah, all for the cash, brutha. Rakin' in the dough, make it rain, holla at ya boy, ya know?"

                                                e "…"

                                                g2 "Ha, spud don’t know. Little pussy if I ever saw one, and I saw plenty, let me tell ya."

                                                g "Haha, you tell him, man."
                                                jump nightclubmenu1
                                                                            
                                            label nightclub_4:
                                                e "I want to talk to your boss."

                                                if(hat < 2):
                                                    g2 "The boss? He don’t want to waste his time on creeps like you."

                                                    e "What, is he scared of me before he meets me? Coward ain’t worth my time, then."
                                                    show boss normal at offscreenright
                                                    show boss normal at right with move

                                                    mb "Not worth your time, am I?"

                                                    e "Oh, shit!"

                                                    g "Boss! We don’t know this guy, he just came in askin' for you."

                                                    mb "I can see that. He must be here for something very important to have the balls to insult me on my own territory. Well, kid, what do ya want?"

                                                    e "Oh, er, um I-"
                                                    menu:
                                                        "Leave":
                                                            e "I’ll just be leaving, then?"
                                                            
                                                            show boss happy
                                                            mb "You think you can insult the next great Capone and get away with it? Waste him, boys."
                                                            play music "gunshot.wav"
                                                            show gangster animated
                                                            show gangster2 animated
                                                            e "Aw, shiiiiiiiii-"
                                                            pause
                                                            stop music 
                                                            play music "scary_music.ogg"
                                                            scene bg death
                                                            pause
                                                            jump choice0_done
                                                        "Ask to be his personal assassin":
                                                            jump nightclub_4_2
                                                        "Punch him":
                                                            jump nightclub_4_3
                                                        "Compliment him":
                                                            jump nightclub_4_4
                                                        "Tell him you're an undercover cop":
                                                            jump nightclub_4_5
                                                                      
                                                elif(hat > 2):
                                                    g "Sorry, bro. That voodoo priest dude high tailed it outta here after you pulled off those mad jukes, bro."
                                                    g2 "Old Capone came back, but he ain’t feelin' so hot after the full fiasco, you know what I’m sayin'?"

                                                    e "Yeah, anyone would be sick after dealing with those wizards."

                                                    g "You got it, bro."
                                                    jump nightclubmenu1
                                                else:
                                                    jump nightclub_5


                                                label nightclub_4_2:
                                                        $ assassin = 1
                                                        e "I’ve come to be your personal assassin."
                                                        
                                                        if(hobo == 3):
                                                            mb "What do you mean? You already killed the hobo. If this is all you wanted, I'm out of here."
                                                            show boss normal at offscreenright with move
                                                            jump nightclubmenu1

                                                        mb "Eh? You want to be my hit man?"
                                                        mb "Well, you do look pretty average… No one would suspect a guy like you to be a stone cold killer."

                                                        e "Yeah, hehe, uh…"
                                                        
                                                        if(hobo == 2):
                                                            mb "I would ask you to assassinate the hobo as a test, but I haven't seen him around lately..."
                                                            mb "What else do you want?"
                                                            show boss normal at offscreenright with move

                                                            e "Oh, hey, I’m alive. How bout that."

                                                            g2 "You got lucky, kid; not many get away so lightly with insultin the boss."

                                                            e "Won’t happen again."

                                                            g "Damn right."
                                                        
                                                            jump nightclubmenu1
                                                            

                                                        mb "Tell ya what: if you prove yourself with an easy hit, I’ll forgive your sorry ass. Whack that annoying ass hobo I keep seein' on the streets."

                                                        e "Eh? You mean that ungrateful sob who treats you like shit if you don’t fork over everything you've got?"

                                                        mb "Yeah, that’s the one. Make it clean, too; get him gone, and don’t leave a trace. Could've just walked outta town, the cops wouldn’t know any better."

                                                        e "Right, discreetly kill the hobo and I’ll earn your trust."
                                                        e "I never thought I’d ever be saying that, but here I am."

                                                        mb "Hehe, you got some spunk kid. Now go show me some discretion."
                                                        menu:
                                                            "Assassinate Lord Hobo":
                                                                $ hobo = 3
                                                                scene bg citysidewalk
                                                                show bryant normal at left
                                                                show hobo normal at right
                                                                e "That's the end for you, you dirty beggar"
                                                                e "DIE MOTHERFUCKER!"
                                                                play music "gunshot.wav"
                                                                show bryant animated at left
                                                                pause
                                                                stop music
                                                                play music "main.ogg"
                                                                jump apartmentn
                                                            "Give the hobo a blank stare":
                                                                scene bg citysidewalk
                                                                show bryant gun at left
                                                                show hobo normal at right
                                                                e "..."
                                                                show bryant normal at left
                                                                e "I can't..."
                                                                e "I just can't do it..."
                                                                e "I love you hobo!"
                                                                e "Everyday I pass by you,I just love your smell."
                                                                e "I'm just attracted to your sexy sexiness, I need you in my life!"
                                                                h "..."
                                                                h "Fuck you man."
                                                                jump map
                                                                
                                                            
                                                        
                                                        show boss normal at offscreenright with move

                                                        e "Oh, hey, I’m alive. How bout that."

                                                        g2 "You got lucky, kid; not many get away so lightly with insultin' the boss."

                                                        e "It won’t happen again."

                                                        g "Damn right."
                                                        
                                                        jump nightclubmenu1




                                                label nightclub_4_3:
                                                        e "I think we should all just calm down, and settle our differences with a peaceful discus-"
                                                        play sound "punch.ogg"
                                                        show bryant punch at center
                                                        

                                                        mb "Never bring a fist to a gunfight, kid. Waste him, boys!"
                                                        play music "gunshot.wav"
                                                        show gangster animated
                                                        show gangster2 animated
                                                        pause
                                                        stop music 
                                                        play music "main.ogg"
                                                        scene bg death
                                                        pause
                                                        jump choice0_done



                                                label nightclub_4_4:
                                                        e "Uhhh, you're lookin' pretty cool, actually. Going for the whole Capone thing, right?"

                                                        mb "Yeah, got these duds a few weeks ago. Felt like I had a business based on his style, why not imitate the guy, right? He was an inspiration."

                                                        e "Yeah…it suits you."

                                                        mb "Thank you. It’s nice to see new kids that have heard of the glorious Capone. You know what, I ain’t gonna kill ya, kid. I’ll be the bigger man this time."

                                                        e "Gee, thanks."

                                                        mb "Enjoy yourself."
                                                        show boss normal at offscreenright with move

                                                        e "Wow, I’m alive after accidentally insulting a mob boss."
                                                        e "Now, moving on to leaving this nightclub alive."
                                                        jump nightclubmenu1




                                                label nightclub_4_5:
                                                        e "Hold it right there, “boss”. I’m actually a cop, and we’ve been lookin' for you for a long time."

                                                        "…"

                                                        "…"

                                                        e "That’s right, you’re all busted. Just hand over your weapons and I’ll-"
                                                        play music "gunshot.wav"
                                                        show gangster animated
                                                        show gangster2 animated
                                                        pause
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done












                                            label nightclub_5:
                                                    g "The boss? Talkin bout the “new boss”?"

                                                    e "Eh? New boss?"

                                                    g "Yeah man, he came outa nowhere and declared himself the new king, or something."
                                                    g2 "Knocked the old boss out cold with voodoo magic or some shit, man. Freaky shit."

                                                    e "He sounds like the guy I want."

                                                    g "Really? You must have balls of steel man, cuz he’s wack."

                                                    show magicianyellow normal at offscreenright
                                                    show magicianyellow normal at right with move

                                                    m2 "See, what are you boys yammerin' about, see?"

                                                    g2 "Oh, shit! Boss! We didn’t mean nothing!"

                                                    m2 "Damn right, ya didn’t, see? And don’t you boys worry, I ain’t here for you, see?"
                                                    m2 "I’m here for that guy der, see?"

                                                    e "You knew I was coming?"

                                                    m2 "I could feel the power, see? The power of the hats is no joke kid, see? You stick out like a sore thumb, see?"
                                                    
                                                    e "What are you doing here? This place doesn’t seem very magician-like."

                                                    m2 "I figure yer all wastin' yer time, playin' around by yourselves, see? Since domination spells like the one you got don’t work, see, I figure I’ll just control ya the good ol fashin way, see, with intimidation and threat of force, see?"

                                                    e "Why do you keep saying see?"

                                                    m2 "Cuz I’m a boss now, see? I’ve read up on your dialect, see, blend right in, don’t I, see?"

                                                    e "What, you watched a bunch of classic mobster movies or something?"

                                                    m2 "…Shut up, see?"

                                                    e "Whatever. I came for your hat, which you can probably tell by now."

                                                    m2 "I see, see? Think you can just wipe out all us magicians and get away with it,see?"

                                                    e "What? No, I just asked them for their hats and they had me pass a test for-"

                                                    m2 "I ain’t fallin' for it, see? Probably knocked ‘em out cold when they weren’t lookin, see? Us magicians are most vulnerable to physical violence, see?"
                                                    e "Uh, so is everyone else."

                                                    m2 "Of course, see? So that means you are too, see?"
                                                    m2 "And you’re here in my new domain, see? With my new armed henchmen here to protect me, see?"

                                                    e "… Now that you mention it…"

                                                    m2 "See, see? You were foolish to come here, mortal, see?"
                                                    m2 "Now, boy, prepare to die, see?!? Get him, boys, see!?!"
                                                    play music "gunshot.wav"
                                                    show gangster animated
                                                    show gangster2 animated

                                                    "OH SHIIII-"

                                                    "*Dodging bullets*"
                                                    stop music
                                                    play music "main.ogg"
                                                    show gangster angry
                                                    show gangster2 angry

                                                    e "…Oh, hey, I’m alive."

                                                    g "Oh, shit boss! He just pulled some matrix shit!"
                                                    g2 "Whoa, he’s showin' more mojo than you do!"

                                                    m2 "…Just a fluke, see? I was goin' easy on him, see?"

                                                    g2 "Eh, boss, we were the ones shootin-"

                                                    m2 "Well shoot again, see?!? Keep doin it until you run out of ammo, see!?!"
                                                    play music "gunshot.wav"

                                                    show gangster animated
                                                    show gangster2 animated
                                                    "*Dodging even more bullets*"
                                                    play music "main.ogg"
                                                    show gangster normal
                                                    show gangster2 normal

                                                    m2 "Wow, that was pretty badass."
                                                    m2 "…see."

                                                    e "Yeah, can you, like, stop shooting me?"

                                                    g "Uh, priest guy, we’re all outta ammo!"

                                                    m2 "…"
                                                    m2 "So, what did you want again, mortal? I suppose I’ll deign to hear you out."

                                                    e "Your hat. That curse is lethal, so I need your hat to reverse it."

                                                    m2 "Oh, right, I suppose it did have that side effect."
                                                    m2 "…Uh, I suppose, uh, I’m generous enough, erm, to comply with your request."
                                                    hide magicianyellow
                                                    show magician normal at right
                                                    $ hat += 1
                                                    m2 "And, uh, actually, I was just planning on leaving, see? Uhhh…"

                                                    e "As long as I have your hat, I don’t care anymore."
                                                    e "Actually, where’s the last guy? The one with the red hat."

                                                    m2 "Eh, him? He’s always down by the cemetery, practicing new spells and such."

                                                    e "Right. I’ll just punch him in the face or something while he’s casting, get the last hat, and reverse this shitty curse."
                                                    e "Oh, you can go now if you want, I guess."

                                                    m2 "…Right, then."
                                                    m2 "Mortals are actually pretty scary…"
                                                    show magicianyellow normal at offscreenright with move

                                                    e "And you guys?"

                                                    g "Woah, dog, you Neo or some shit, we ain’t gonna mess with you."
                                                    g2 "Yeah, man, those were some sweet moves, brah."

                                                    e "Oh, all “cool” now after unloading all your ammo at me eh?"

                                                    g "Ay man, he was threatenin us with all his voodoo shit, man, cut us some slack."
                                                    g2 "Yeah, now that you scared him off we’re Capone’s crew again, wherever he is."
                                                    g "Voodoo guy gave him a nasty ass cold, brutha. Sick shit, literally."
                                                    
                                                    e "Well, enjoy yourselves I guess. I’m going to go home and have a nervous breakdown about what just happened."
                                                    
                                                    g "Peace out, dog."
                                                    g2 "Yeah, come back anytime. We’ll hang with ya."

                                                    e "Yeah… maybe."
                                                    jump apartmentn




                                            label nightclub_6:
                                                    e "Hold it, “dawgs”, I’m an undercover cop!"
                                                    e "You’re all under arrest! Drop your weapons and put your hands in the a-"
                                                    play music "gunshot.wav"
                                                    show gangster animated
                                                    show gangster2 animated
                                                    pause
                                                    stop music 
                                                    play music "scary_music.ogg"
                                                    scene bg death
                                                    pause
                                                    jump choice0_done


                                                                            

                                                

                                elif result == "policestation":
                                    scene bg policestation
                                    show bryant normal at right
                                    show policeman normal at left
                                    e "Ok, I’m at the police station. Now what?"
                                    p "Hello there, sir. Can I help you with something?"
                                    label pschoice:
                                        scene bg policestation
                                        show policeman normal at left
                                        show bryant normal at right
                                        menu:
                                            "Go back outside":
                                                e "No thanks, I’m good."
                                                jump map
                                            "Turn yourself in":
                                                jump choice8_turnin
                                            "Ask about magicians":
                                                jump choice8_ask
                                            "Ask for a gun":
                                                jump choice8_gun
                                            "Report a crime":
                                                jump choice8_report
    
                                        label choice8_turnin:
                                            e "I’d like to turn myself in."
                                            p " Oh, my. For what?"
                                            menu:
                                                "Take it back":
                                                    jump choice9_takeitback
                                                "Wasting time":
                                                    jump choice9_time
                                                "Being too sexy":
                                                    jump choice9_sexy
                                                "Attempted murder":
                                                    jump choice9_murder
                                                "Littering":
                                                    jump choice9_littering
                                            label choice9_takeitback:
                                                e "Haha, just kidding."
                                                show policeman angry at left
                                                p "Please don’t joke like that, sir. Sometimes we actually do get the occasional guilty fellow that warrants attention."
                                                e "You’re right... Sorry."
                                                p "Anything else?"
                                                jump pschoice
                                            label choice9_time:
                                                e "For wasting an officer’s time."
                                                p "Eh?"
                                                p "..."
                                                p "Oh... I get it. Hah."
                                                p "We made a new law yesterday."
                                                p "If the officer laughs about it, you’re free to go."
                                                e "Well, good for me."
                                                p "Indeed. Seriously, though, do you need anything?"
                                                jump pschoice
                                            label choice9_sexy:
                                                e "I’m just too hot, officer."
                                                p "Excuse me?"
                                                e "It should be illegal to look as good as I do. My guilty conscience can no longer tolerate how unfairly distracting I am to the opposite sex."
                                                show policeman angry at left
                                                p "Sir, stop. Please."
                                                e "What do you mean? I’m already on the most-wanted list of every lady in town."
                                                p "Sir, I’m warning you..."
                                                e "Cage me, officer. That is, if you think mere bars of iron can contain this godly form."
                                                
                                                p "Sir, stop, or I will shoot."
                                                e "Fine."
                                                p "... Anything else?"
                                                jump pschoice
                                            label choice9_murder:
                                                e "I tried to murder someone."
                                                p "Who?"
                                                e "Uhhh... ummm... That hobo whose been begging for money daily. I beat him within an inch of his life."
                                                p "Oh, just him? Don’t worry. Ungrateful little shit, I gave him 5$ just to shut him up one day and he called me a cheapskate. Almost pulled my gun out on him right then and there."
                                                e "Wait, what? You are a real police officer, correct?"
                                                p "Yeah, yeah. I'm just saying that you’re in good company."
                                                p "Just between you and me, everyone here at the force wouldn’t look too deeply into it if he went missing. If you know what I mean..."
                                                e "You can’t be serious..."
                                                p "Just putting it out there. Is there anything else on your mind?"
                                                jump pschoice
                                            label choice9_littering:
                                                e "I littered."
                                                e "..."
                                                e "I threw a bottle, like, right next to the sign that said $100 fine for littering, when no one was looking."
                                                p "... And you’re actually asking to be arrested for this?"
                                                e "Yes. I committed a crime and I need to be punished."
                                                p "Uh, as long as you feel sufficiently guilty about i-"
                                                e "NO. Punish me!"
                                                p "Er... Right. If you can’t pay the $100 fine, I guess I’ll have no choice but to bring you in."
                                                menu:
                                                    "Pay":
                                                        jump choice10_pay
                                                    "Don't pay":
                                                        jump choice10_nopay
                                                    "Bribe him":
                                                        jump choice10_bribe
                                                label choice10_pay:
                                                    if (money >= 100):
                                                        $ money -= 100
                                                        e "Here’s your money, you capitalist pig."
                                                        p "Excuse me, sir?"
                                                        e "You heard me, thief. $100 for littering? It's disgusting how our country tolerates such a corrupt system of organized extortion."
                                                        p "Sir, you just-"
                                                        p "..."
                                                        p "Nevermind..."
                                                        e "What was that?"
                                                        p "Nothing, sir. Now that that’s all sorted out, is there anything else you need?"
                                                        jump pschoice
                                                    else:
                                                        e "I’ll pay the fi-"
                                                        e "Oh wait, I don’t have enough money on me."
                                                        p "So you don’t have enough to cover the fine?"
                                                        e "Nope."
                                                        p "I guess we’ll have to arrest you then."
                                                        e "Yeah, it seems so."
                                                        p "For a $100 fine, I’d say an overnight stay in a cell should do it."
                                                        jump map
                                                label choice10_nopay:
                                                    e "I have no funds to cover the cost of my heinous crimes. I must be incarcerated."
                                                    p " ... Ok then, I guess we’ll hold you in one of our cells overnight."
                                                    e "Yes, very good. A long night in a cold damp cell oughta sort me out."
                                                    p "Sir, is there any reason you’re doing this?"
                                                    e "Doing what?!?"
                                                    p "... Nevermind. Follow me."
                                                    scene bg jail
                                                    show bryant normal at left
                                                    show policeman normal at right
                                                    "*Hours later*"
                                                    p "You’re free to go."
                                                    e "WHAT? It hasn’t been a full day yet. I haven’t learned my lesson."
                                                    p "Uh, we’re letting you out early for good behavior."
                                                    e "Oh, this is bullshit. I’m getting released early after pleading guilty to a crime. I’ll get spoiled under such a lax system. I’ll start considering murder next!"
                                                    p "Sir, none of us here at the force can understand why you’re doing this. Please. Just go home."
                                                    e "NO. PUNISH ME."
                                                    p "Sir, get out."
                                                    e "Such a weak system... Soft on crime... They should bring back the death penalty... grumble grumble."
                                                    e "I’ll be back here, you’ll see! You’ll wish you shot me down here and now."
                                                    p "I do, sir. Now, go back home."
                                                    jump apartmentn
                                                label choice10_bribe:
                                                    if (money >= 200):
                                                        $ money -= 200
                                                        e "Woah. Hey now officer, don’t be so hasty."
                                                        e "How’s about I just give you this brand new $100 bill, and you look the other way?"
                                                        p "..."
                                                        p "Sir, are you trying to bribe me?"
                                                        e "Wow, what a smart guy. You saw right through me. Tell ya what, I’ll throw in another hundred. What do you think?"
                                                        p "Sir..."
                                                        p "..."
                                                        p "Uh... Ok then, I guess $200 will do it."
                                                        e "Here you are, officer. Smart man. This will blow over quick, don’t you worry. I’ll keep my head down from now on... Maybe I'll move outta town."
                                                        p "Uh... yeah... You do that."
                                                        p "Um, anything else?"
                                                        jump pschoice
                                                    else:
                                                        e "Woah. Hey now officer, don’t be so hasty."
                                                        e "How’s about I just give you this brand new $100 bill, and you look the other way?"
                                                        p "..."
                                                        p "Sir, are you trying to bribe me?"
                                                        e "Wow, what a smart guy. You saw right through me. Tell ya what, I’ll throw in another hundred, whatdayasay?"
                                                        p "... Is this a test? Am I being watched?"
                                                        e "No ones gonna know, officer. I ain’t no rat."
                                                        p "No way. Forget it. Just keep your money and go away."
                                                        e "That works too, I guess."
                                                        p "Then... uh... Anything else?"
                                                        jump pschoice
                                        label choice8_ask:
                                            e "I’m looking for a bunch of weirdos in silly hats. Have you heard of anyone like that?"
                                            
                                            if(hat > 0):
                                                p "Yeah, but he left awhile ago."
                                                p "Anything else?"
                                                jump pschoice
                                                
                                            if choice8b:
                                                p "Actually, we just got a person like that holed up in custody."
                                                p "He was yelling gibberish about dolls and the lack of customer service at a self-serve gas pump while trying to fill up some sort of water bottle."
                                                p "Is he a friend of yours?"
                                                e "Erm, an acquaintance. Kind of."
                                                p "Good enough. I’ll bring you to him."
                                                scene bg jail
                                                show magiciangreen normal at right
                                                show bryant normal at left
                                                m4 "-and my sundial doesn’t even work in here! How am I supposed to tell when second breakfast is occurring? Simply outrageous!"
                                                m4 "Oh, it's you. Have you come to deliver the requested tomes?"
                                                e "Do you remember me?"
                                                m4 "Of course. An elephant never forgets, and I, a magician, being at least equal to an elephant in every way, do so as well."
                                                m4 "Wait, what were you here for again?"
                                                label jailchoice:
                                                    menu:
                                                        "Leave":
                                                            e "Nothing, really. See you later."
                                                            m4 "Oh. Bye. Be sure to get those books soon. You can never stock enough on puppet psychology."
                                                            scene bg policestation
                                                            show bryant normal at right
                                                            show policeman normal at left
                                                            p "Are you done talking with him, then?"
                                                            e "Yep."
                                                            p "Alrighty. Do you need anything else while you’re here?"
                                                            jump pschoice
                                                        "Ask how he got arrested ":
                                                            jump choice11_how
                                                        "Punch him in the face ":
                                                            jump choice11_punch
                                                        "Ask about the curse ":
                                                            jump choice11_curse
                                                        "Ask for his hat ":
                                                            jump choice11_hat
                                                    label choice11_how:
                                                        e "How did an all-powerful magician get arrested?"
                                                        m4 "Eh? All-powerful doesn’t mean all-abusing. They were coming at me with pitiful little guns. It was almost laughable."
                                                        m4 "I feigned surrender just to mock them, and they seemed to realize immediately the difference in our powers."
                                                        m4 "They brought me here, obviously to declare me the new ruler of your country, but the conditions here are just so bare and tasteless."
                                                        m4 "If this is how you treat your soon to be new leader, I can scarcely imagine how you all managed to live so long without starving to death."
                                                        e "That makes two of us."
                                                        m4 "So, soon to be subject, what do you desire of me?"
                                                        jump jailchoice
                                                    label choice11_punch:
                                                        play sound "punch.ogg"
                                                        show bryant punch at center
                                                        pause
                                                        show bryant normal at left
                                                        m4 "OW! Owww..."
                                                        e "Who's the all-powerful magician now, asshole?"
                                                        m4 "Urg... Still me of course, I’m just counter casting your physical damage with... uh... a holy mantra. A puppet mantra. Yeah. "
                                                        play sound "punch.ogg"
                                                        show bryant punch at center
                                                        pause
                                                        show bryant normal at left
                                                        m4 "Owwww OWWWW THAT STINGS!!!"
                                                        p "HEY! Are you assaulting the weirdo?"
                                                        e "Oh shit! That’s right... This is still a police station..."
                                                        m4 "HaHA! Yes, my minions, take him away. Lucky you, boy. My curse was almost complete, but I’ll let my new servants punish you in my stead."
                                                        p "Knock it off, tough guy. I don’t know what your deal with him is, but you can cool your jets in a cell for a while."
                                                        e "Aw come on, he deserved it."
                                                        p "The law says otherwise. We’ll let you go at sunset, if you can keep your fists to yourself."
                                                        e "Ugh... Damn cops and their dislike of old fashioned justice..."
                                                        jump apartmentn
                                                    label choice11_curse:
                                                        if (knowledge == 0):
                                                            e "Did you curse me?"
                                                            m4 "Hm? You? Yeah."
                                                            e "Well, what the hell!"
                                                            m4 "You were being very disrespectful, you know. We all thought this would be the best way for you to learn."
                                                            e "But now I keep doing unnatural things for no apparent reason!"
                                                            m4 "Well, now you know how a puppet feels when some newbie jerks him around by the strings till he breaks. It sucks, doesn't it?"
                                                            e "Well, undo it!"
                                                            m4 "Nope. Not until you learn to show puppets a little more respect for what they’ve been through. It’ll wear off on its own anyways, quit being a baby about it."
                                                            jump jailchoice
                                                        else:
                                                            e "You brainwashed me! Now I have to do whatever some unknown force tells me to do."
                                                            m4 "Actually we found out about the whole “unknown force thing”."
                                                            m4 "Turns out all the orders were coming from those jerks who made the stonehenge. "
                                                            m4 "Those \"White Knight\" pricks didn’t like spells that enslaved the general populace, so they jinxed all the good curses to make it so they got the control instead of us."
                                                            m4 "So we just started mass enslaving people till they were so overflowed with orders that they just stopped caring about how good they were being."
                                                            m4 "It's still a loss, since we can’t have human puppets anymore, but at least we annoyed them."
                                                            e "So how is this supposed to show me how it feels to be a puppet?"
                                                            m4 "Oh. Uhhh..."
                                                            m4 "Well you’re still under someone else's control, aren’t you?  Sucks, don’t it?"
                                                            e "Yeah, I guess."
                                                            m4 "Well thats how a puppet feels... Like every day. Tough it out, wimp. Show some respect."
                                                            jump jailchoice
                                                    label choice11_hat:
                                                        m4 "Eh? Why?"
                                                        if (knowledge < 2):
                                                            e "Um, uhhh..."
                                                            e "Cuz I think green suits me better?"
                                                            m4 "First you’re dissing the puppets, now you think I’ll give my hat away so easily?"
                                                            e "Come on, you already have a mask... How much headwear do you need? You’ll still look plenty weird without it, don't worry."
                                                            m4 "Go away, or I shall curse you a second time."
                                                            jump jailchoice
                                                        else:
                                                            e "I need your hats, or your curse will kill me, remember?"
                                                            m4 "Eh? What do you-"
                                                            m4 "Ohhhh... Oh right. THAT."
                                                            m4 "Forgot about that."
                                                            e "You just “forgot” about a curse being lethal?"
                                                            m4 "Well, it's just a minor side-effect. Barely worth mentioning in most cases."
                                                            e "What?!?"
                                                            m4 "Uh, not in this case, I suppose. At least on your end."
                                                            e "So come on, hand over the hat."
                                                            m4 "Wait, I can’t just “hand over the hat” for a minor mistake. Come on now."
                                                            m4 "It's my pride and joy. I’ve been wearing it since my first act of puppeteering. I had my first puppet put it on my head for me! Oh, the memories..."
                                                            e "I’m going to die if I don’t have it! Or can you undo the curse somehow?"
                                                            m4 "I can’t undo it at this point, and I can’t just give the hat away for free..."
                                                            m4 "How’s about you earn it first?"
                                                            e "Earn it?"
                                                            m4 "Yeah, how about a three-question quiz?"
                                                            m4 "The curse was to teach you how a puppet feels; more about our wonderful wizarding culture."
                                                            m4 "If you prove you’ve learned something, I’ll help undo the curse by giving you my hat."
                                                            e "Your wizarding culture? You curse people for the most minor slights and apparently value your hat more than my life."
                                                            m4 "Wow, you actually just answered two of the questions I was about to ask you."
                                                            m4 "..."
                                                            m4 "The final question then: What less famous group did us puppeteers originally diverge from?"
                                                            menu:
                                                                "Leave":
                                                                    jump choice12_leave
                                                                "I don’t know":
                                                                    jump choice12_dunno
                                                                "Alchemists":
                                                                    jump choice12_alchemists
                                                                "Witches":
                                                                    jump choice12_witches
                                                                "Punch him and take the hat":
                                                                    jump choice12_punch
                                                            label choice12_leave:
                                                                e "Nevermind, there’s something else I have to do."
                                                                m4 "Eh? Aren’t you going to die without my hat? It's just a simple quiz."
                                                                e "I’ll be back for it, don’t worry."
                                                                scene bg policestation
                                                                show bryant normal at left
                                                                p "Done talking with him?"
                                                                e "For now."
                                                                p "Well then, anything else you need before you go?"
                                                                jump pschoice
                                                            label choice12_dunno:
                                                                e "I don’t know, just give me the hat."
                                                                m4 "Nope, sorry. Can’t just give away my precious hat for no reason, it’d shame my wizarding name."
                                                                e "Come on, I’m going to die without it!"
                                                                m4 "Well, you deserve to, if you can’t even answer such a simple question."
                                                                m4 "I would think it’d be common sense by now. Education nowadays, I bet they aren’t even teaching AP puppeteering anymore."
                                                                m4 "Hmph. Well then, I refuse to surrender my hat. Deal with it. Hmph."
                                                                jump jailchoice
                                                            label choice12_alchemists:
                                                                e "Alchemists, right?"
                                                                m4 "Yeah, that’s right. We had to learn to turn stone into gold before we moved on to useful things like making puppets dance."
                                                                m4 "Well, it seems to me like you’ve learned a lot about being a puppet since we’ve cursed you, so I’ll do my part in helping you break it off early."
                                                                m4 "Take my hat, and keep it well."
                                                                hide magiciangreen
                                                                show magician normal at right
                                                                $ hat += 1
                                                                e "Great, one down, three to go!"
                                                                e "Speaking of which, I still need your friends' hats. Do you know where they are?"
                                                                m4 "I’m not sure, they’ve kept me here as ruler for so long that I can’t say I do."
                                                                m4 "Actually, I remember the blue hat guy raving about some type of food source you humans eat, so you’ll probably find him eating somewhere."
                                                                e "\"Blue hat guy\"? You don’t know his name?"
                                                                m4 "Not really."
                                                                m4 "They just drag me around everywhere, and I follow out of peer-pressure."
                                                                m4 "(They’re kinda weirdos, between you and me.)"
                                                                m4 "Anyway, he’ll probably want you to prove yourself to him too, so just explain things to him and prepare to do another quiz or something."
                                                                e "It’s getting late, so I’ll be heading home first. Thanks for the hat, green hat guy."
                                                                m4 "Go forth, young lad, and with your newfound respect for puppets you will surely earn your life back."
                                                                m4 "Meanwhile, I suppose I can tolerate serving as your new ruler for a while, at least till I grow too bored."
                                                                e "Right. You do that."
                                                                jump apartmentn
                                                            label choice12_witches:
                                                                e "Witches?"
                                                                m4 "Wit- WHAT?"
                                                                e "Those witches they hunted back in the 1600’s, right? The Salem trials, or whatever they were?"
                                                                m4 "Oh hell no, we’ve had and will have nothing to do with those disgusting mockeries. You’re trying to mock me, aren't you?"
                                                                e "No, I really don’t care. Just give me the hat, dammit."
                                                                m4 "No! If you haven’t learned anything, then I’m not helping you break the curse! Hmph."
                                                                jump jailchoice
                                                            label choice12_punch:
                                                                e "Heres what I think of your stupid quiz!"
                                                                play sound "punch.ogg"
                                                                show bryant punch at center 
                                                                pause
                                                                show bryant normal at left
                                                                m4 "OW! Owww..."
                                                                e "Who's the all powerful magician now, asshole? Now hand over the hat already!"
                                                                m4 "Urg... attacking a humble magician in his blind spot. Do you humans have no honor? You totally fail the quiz, by the way. That answer was nowhere near."
                                                                e "Your blind spot? I punched you in the face."
                                                                m4 "You think I can see out of this mask? It doesn’t have eye holes, fool."
                                                                show policeman angry at offscreenright
                                                                show policeman at center with move
                                                                p "HEY. Are you assaulting him?"
                                                                e "Oh shit! That’s right, this is still a police station."
                                                                m4 "Ah yes, guards! Take him away, to wherever you bring people who fail simple quizzes!"
                                                                p "Knock it off, tough guy. I don’t know what your deal with him is, but you can cool your jets in a cell for a while."
                                                                e "Aw come on, he deserved it."
                                                                p "The law says otherwise. We’ll let you go at sunset, if you can keep your fists to yourself."
                                                                e "Ugh... Damn cops and their dislike of old fashioned justice..."
                                                                jump apartmentn
                                        label choice8_gun:
                                            e "Can I have a gun?"
                                            p "You mean a permit?"
                                            e "No, just borrow a gun."
                                            e "..."
                                            e "I’ll only need it for like 5 minutes, there’s this guy outside who-"
                                            p "No. Just no."
                                            p "Do you ACTUALLY need anything from us, sir?"
                                            jump pschoice
                                        label choice8_report:
                                            e "I’d like to report a crime."
                                            p "Yes?"
                                            e "A group of wizards cursed me. Now I’m forced to do whatever an unknown force wills me to do."
                                            p "..."
                                            p "Sir, that’s not funny. We get actual reports here, we don’t have time to joke around like that."
                                            e "But it really happened!"
                                            e "(Well of course they don’t believe it. I guess I’ll have to solve this problem myself.)"
                                            p "Just don’t joke around like that. Do you really need something here?"
                                            jump pschoice
                                            
                                            
                                                                
                                                                
                                                                
                                                                
                                                            

                                    
                                return
                        
                                pause
                                jump choice0_done
                                
                                
    label choice0_young:                #If you are younger than 18
        play music "main.ogg"
        scene bg apartmentday
        show bryant normal
        "This is Bryant Day; He’s an average man, living an average life in an average city with an average job."
        "He’s mediocre, undistinguishable, ordinary, unremarkable, indifferent, lackluster, and forgettable."
        "And he’s proud of it."
        scene bg citysidewalk 
        show hobo angry at right
  
    
        "Bryant kept his head down all his life; He stays out of fights, keeps an average amount of friends, watches all the popular shows, eats only typical food."
        "If ever there was a standard for the most average human in existence, Bryant would have the high score."
        init:
            $ move = MoveTransition(1.0)
        show bryant normal at offscreenright with move
        show bryant normal at right with move
        show bryant normal at center with move
        show bryant normal at left with move
        "He aims to stay at the top. Well, not the very top: he can’t get too good at something."
        scene bg bookstore2
        show bryant normal at left
        show eve normal at offscreenright 
        "Here, as an average retailer in an average bookstore, Bryant Day wi-"
        show eve normal at right with move
        show eve normal at center with move
        l "Bryant, help me sort these new books out. I already know where most of them are going."
        "That’s Bryant’s best friend, Eve."
        "She’s the manager of this store, and has practically memorized everything there is to know about the store's inventory."
        l "Bryant, what are you doing?"
        e "Just having an internal monologue about how awesomely average my life is."
        l "…Whatever I guess."
        show eve normal at right with move 
        show eve normal at offscreenright with move
        "She’s a bit too smart for Bryant’s taste, but not everyone can be as average as himself."
        "But here, as an average retailer in an average bookstore, Bryant Day will live out the rest of his average life in an average manner."
        "He will retire after an average number of years to raise an average number of children,"
        "and die at the average life expectancy, forever to rest in an average grave."
        "Hooray for low expectations!"
    
        "At least, that’s the plan."
        #Marco: 10/6/2013 at 11:54 AM made grammatical changes to script thus far.
        play music "energetic_music.ogg"
        
        show magicianred normal behind bryant:
            xalign .9 yalign .7
        show magicianblue normal behind bryant:
            xalign .7 yalign .7
        show magiciangreen normal behind bryant:
            xalign .5 yalign .7
        show magicianyellow normal behind bryant:
            xalign .3 yalign .7

        
        m "This is an outrage!"
        e "What can I help you with s-"
        m2 "Those ingrates at the so called “magician shop” across the street dare to call themselves first rate when they don’t even have a spare supply of Ether to sell!"
        m2 "They're trying to give me a gimmick along with just magic wands and those barely enchanted playing cards. Why I had better tools when I was just a wee lad playing with dolls!"
        m3 "Next time, we will NOT be buying anything in their shop, let me tell you."
        e "That is interesting but also seems irrelevant."
        m4 "Quite true, unlike the blatant false advertising etched into this book we purchased."
        e "\" Dolls and Boys: Psychological studies on a young one’s development cycles\" What was wrong with it?"
        m4 "It only talked about the humans growing up or something, nothing at all about the doll’s thoughts at all."
        m4 "There always seems to be an unfair bias towards humans in these kind of books."
        m "I suspect racism!"
        m2 "We demand reparation in the form of what we expected!"  
        m3 "Some form of writing regarding the mental state of the Homo Mannequinious!"
        e "Wait, are you trying to return this? The receipt says it’s from Borders, and they went out of business a while ago."
        m "Blatant racism!"
        m2 "See here, petty mortal, the inner workings of puppets and mannequins could span eons worth of physical pages, and with a rich history that could possibly dwarf all of your \"modern era\"."
        m2 "They’re quite good conversationalists as well, I would know."
        m3 "I’ve been talking to puppets since I was born."
        m3 "Enough of your ignorant prattle, not having any tomes on this glorious matter would be a shame to this establishment and anyone within eyeshot of it."
        e "I just checked our records, and I really don’t think we have any books concerning a subject that doesn’t exist."
        "..."
        m "You dare to belittle our glorious art?"
        m "After all the countless perfect puppets we’ve created?"
        m "Do you suggest that there’s nothing to write about their wonderful and completely existent thought process?"
        m2 "Are you mad?"
        m3 "Perhaps he’s mocking us out of jealousy..."
        m4 "Or maybe out of fear..."
        m "Regardless of your motives, your implied ignorance is an affront to our very lifework."
        m "If you’re so insistent that a puppet is mindless let’s see how you feel being one!"
        show magicianred casting behind bryant:
            xalign .9 yalign .7
        show magicianblue casting behind bryant:
            xalign .7 yalign .7
        show magiciangreen casting behind bryant:
            xalign .5 yalign .7
        show magicianyellow casting behind bryant:
            xalign .3 yalign .7
        play sound "spell.ogg"
        "..."
        e "Anything else I can help you with?"
        m2 "Not really I guess. We appreciate the quick service."
        m "But we’ll be back in a century or two, be sure to expand your inventory by then."
        e "Sure thing, sir."
        show magicianred normal at offscreenright with move
        show magicianblue normal at offscreenright with move
        show magiciangreen normal at offscreenright with move
        show magicianyellow normal at offscreenright with move
        play music "main.ogg"
        e "Well then, that was very un-average."
        e "But who cares, I guess..."
        show eve normal at right with move
        l "If you’re done talking with those un-average gentlemen, could you carry an average amount of average books to their respectively average piles already?!"
        e "I can use synonyms, if it’s starting to get on your nerves."
        scene black with dissolve
        "Tap to continue ..."
    
    #Marco: edited more errors on 10/6/2013 4:44 pm
    

    
    
        scene bg apartmentnight
        show bryant normal
        e "Well, besides those weirdoes, it was another perfectly average day."
        e "Now, time for an average night’s sleep."
        scene bg apartmentnight with dissolve
        scene black with dissolve
        stop music 
        play sound "spell.ogg"
        #pause
        scene black with dissolve
        "Tap to continue..."
    
        scene bg apartmentday
        show bryant normal
        e "Looks like another gloriously ordinary day is afoot."
        e "I guess I’ll -"
        menu:
            "sleep in a little.":
                jump choice1_sleep2
            "go out to work.":
                jump choice1_work2
        label choice1_sleep2:
            $ weirdness += 1
            scene bg apartmentday
            show bryant angry
            e "fall back asleep? I usually head out to work now, but I guess I’m too tired."
            scene black with dissolve
            pause 3.0
            scene bg apartmentday 
            show bryant angry
            e "Oh poop, now I’m late! I shouldn’t have wasted so much time in bed!"
            jump choice1_done2
        label choice1_work2:
            jump choice1_done2
            label choice1_done2:
                
            scene bg citysidewalk
            show bryant normal at left
            show hobo normal at right
            e "Oh geez, that beggar is still here."
            h "Hey you, got any change?"
        menu:
            "Just keep walking to work.":
                jump choice2_walkaway2
            "Give him some pocket change.":
                jump choice2_givemoney2
            "Tell him to get a job.":
                jump choice2_getajob2
        label choice2_walkaway2:
            jump choice2_done2
        label choice2_givemoney2:
            $ weirdness += 1
            show hobo angry at right
            h "What, just this? Gimmie a 10, I’ve fought in every war there was!"
        menu:
            "Walk away.":
                jump choice3_done2
            "Give him $10 more.":
                jump choice3_more2
            "Tell him to go earn it.":
                jump choice3_getajob2
        label choice3_more2:
            $ weirdness += 1
            e "Fine, here’s another $10."
            show hobo happy at right
            h "About darn time someone gave me the respect I deserve. *grumble grumble*"
            e "Why did I do that? I’ve been ignoring him for months now."
            jump choice3_done2
        label choice3_getajob2:
            jump choice2_getajob2
        label choice2_getajob2:
            $ weirdness += 1
            e "Why don’t you go earn it, you dirty beggar?"
            show hobo angry at right
            h "You’re more dirty than me, you ungrateful little runt! *grumble grumble*"
            e "Why did I say that? I’ve been ignoring him for months now."
            jump choice2_done2
            label choice3_done2:
                jump choice2_done2
            label choice2_done2:
        
            scene bg bookstore1
            show bryant normal at left
            if (weirdness > 0):
                e "Well, now that I’m here, at least the rest of the day will go normally."
            else:
                e "I’ll have to make this day twice as average as usual, to make up for yesterday."
            e "Here comes a customer now."
            show citizen normal at offscreenright with move
            show citizen normal at right with move

            c "Excuse me, do you know where the history section is?"
                #Marco: just gunna leave a suggestion here, in the beginning of the scene, just show bryant then after he says his two lines, have the customer enter the scene on the right.
        menu:
            "Tell him where it is.":
                jump choice4_normal2
            "Insult him for being so helpless.":
                jump choice4_insult2
            "Recommend a better subject than history.":
                jump choice4_subject2
        label choice4_normal2:
                e "Right over there, sir. You can see the sign from here."
                c "Ah, thank you."
                jump choice4_done2
        label choice4_insult2:
                $ weirdness += 2
                e "Under the big sign that says history, dumba**."
                c "Well, I never!"
                show bryant normal at left with move
                show bryant normal at offscreenleft with move
                c "Wait, What?!?"
                jump choice4_done2
        label choice4_subject2:
                $ weirdness += 1
                e "Nobody cares about history nowadays, try going to the cooking section over there instead."
                c "Uh, um, er..."
                show citizen normal at right with move
                show citizen normal at offscreenright with move
                e "Wait, why would I say that?"
                jump choice4_done2
        label choice4_done2:
                scene bg bookstore2
                show bryant normal at right
                show eve normal at left
                l "Bryant, you're not working with any customers, right? Come help me with these books."
        menu:
            "Help her.":
                jump choice5_normal2
            "Don’t help her.":
                jump choice5_bad2
            "Tell her off.":
                jump choice5_vbad2
        label choice5_normal2:
                e "Sure, as long as my part is as average as it was yesterday."
                l "You never shut up about averageness, do you?"
                e "It’s my thing. Why can’t you accept me for the average man I am, Eve?!"
                l "Be quiet, you!"
                jump choice5_done2
        label choice5_bad2:
                $ weirdness += 1
                e "Eve, you do realize I’m paid to work the register around here right? Not heavy lifting!"
                show eve angry at left
                l "What?"
                l "I only have a few books left, it’ll only take a second if you help me."
                e "It's not in my job description."
                l "Whatever, jerkwad."
                e "Wait, what the hell?! I’ve always been helping Eve with chores!"
                e "What’s gotten into me?"
                jump choice5_done2
#Marco: fixed grammatical errors up to here on 10/6/2013
        label choice5_vbad2:
                $ weirdness += 2
                $ evepissed += 1
                e "Eve, why don’t you do my job for a change? You're always expecting me to drop everything I’m doing for your convenience!"
                "..."
                show eve angry at left
                l "What the heck, Bryant!? I was the one who recommended you to the manager in the first place, and now you’re suddenly an ungrateful ba***** who can’t deign to carry a few books between customers?"
                l "Fine then, f*** you. A**hole."
                e "What the heck!? Eve is my best friend, why did I insult her like that?"
                jump choice5_done2
        label choice5_done2:
            if (weirdness == 0):
                scene bg apartmentsunset
                show bryant normal
                e "Seems today was another average day after all. Those weirdoes couldn’t corrupt my averageness after all."
                e "Everything turned out all right, I guess..."
                e "Now, to repeat until I die of old age."
                stop music
                play music "scary_music.ogg"
                scene bg death
                pause
                jump choice0_done
            elif (weirdness < 4):
                scene bg apartmentsunset
                show bryant normal
                e "That’s so odd, I was doing some really uncharacteristic things today."
                e "Now that I think about it, I couldn't even remember my train of thought when I was doing these actions. It’s like I just felt a random impulse and did it."
                e "It seems unlikely, but maybe those magician weirdoes did something to me when they were casting that spell?"
                e "I mean, maybe they secretly drugged me or something while they pretended to ‘cast a spell’ on me? I can’t think of anything else that could have made me do that stuff."
                e "I have the rest of the week off, I guess I can look up more about them in my spare time."
                e "Actually, maybe Eve knows about them."
                e "I remember she saw them, she might even know more about that doll cult or whatever they were blabbing about."
                e "First thing tomorrow, I’ll go to the book-store and ask her about it."
                scene black
                "Tap to continue ..."
                play sound "spell.ogg"
            elif (weirdness >= 4):
                scene bg apartmentsunset
                show bryant normal
                e "Okay, what the hell?!"
                e "I could never imagine myself doing half those things, but I just did them all at the same time, and I don’t even know why."
                e "It’s like I just got these random impulses to do irregular things, and I did them without thinking about it until afterwards."
                e "This is freaky and dangerous. I feel like I don’t have control over what I’m doing anymore."
                e "Wait! Those magician weirdoes yesterday, didn’t they cast some sort of puppet spell on me?"
                e "I’d never believe in unaverage junk like that working in a million years, but could my random actions today possibly be proof? I’ve got to be sure!"
                e "I have the rest of the week off..."
                e "I know Eve saw them, maybe she saw what they were doing when the magicians were pretending to cast a spell on me."
                e "I’ve got to ask her about it tomorrow. For now, I’ve got to rest my mind from all of this disgusting unaverageness."
                scene black with dissolve
                "Tap to continue ..."
                play sound "spell.ogg"
            screen example_imagemap2:
                            imagemap:
                                ground "cityoverview.png"
                                hover "cityoverviewfocused.png"

                                hotspot (216, 212, 124, 42) action Return("bookstore")
                                hotspot (328, 140, 124, 42) action Return("alley")
                                hotspot (354, 328, 124, 42) action Return("apartment")
                                hotspot (460, 188, 124, 42) action Return("bank")
                                hotspot (465, 48, 124, 42) action Return ("burgerstore")
                                hotspot (328, 22, 124, 42) action Return ("cemetary")
                                hotspot (454, 386, 124, 42) action Return ("sidewalk")
                                hotspot (626, 444, 124, 42) action Return ("statue")
                                hotspot (598, 342, 124, 42) action Return ("nightclub")
                                hotspot (184, 346, 124, 42) action Return ("policestation")
                            text ("Days left: %d" % (daysleft)) size 30 xalign 0.5 yalign 0.99
                            text ("Hats collected: %d" % (hat)) size 25 xalign 0.5 yalign 0.9
                            #ui.text("Days Left: %(daysleft)d", size=40, xalign=0.5)
        
        
            label map2:
    
                                call screen example_imagemap2
    
                                $ result = _return
    
                                if result == "bookstore":
                                    scene bg bookstore1 
                                    show bryant normal at left
                                    e "It’s my week off, but I’m still allowed to come here of course."
                                    e "Now that I’m here, I’ll..."
                                    label bschoice_a2:
                                        scene bg bookstore1
                                        show bryant normal at left
                                        menu:
                                            "Go back outside":
                                                e "Go right back outside. Ok then."
                                                jump map2
                                            "Go see Eve":
                                                jump choice14_eve2
                                            "Read some books ":
                                                jump choice14_books2
                                            "Work":
                                                jump choice14_work2
                                            "Set the whole Bookstore on fire ":
                                                jump choice14_fire2
                                        label choice14_eve2:
                                            e "Eve, it’s me."
                                            if (evepissed >= 1):
                                                show eve angry at right
                                                l "What do you want, asshole?"
                                                e "Oh right, I pissed her off yesterday, didn’t I?"
                                            else:
                                                show eve normal at right
                                                l "Bryant? I thought it was your week off."
                                            e "Eve, I-"
                                            label bschoice_b2:
                                            menu:
                                                "Run away":
                                                    e "Gotta go fast!"
                                                    show bryant normal at left with move
                                                    show bryant normal at offscreenleft with move
                                                    if (evepissed >= 1):
                                                        l "Damn right you run..."
                                                        jump map2
                                                    else:
                                                        l "That’s unaverage of him..."
                                                        jump map2
                                                "Explain the situation ":
                                                    e "I need your help."
                                                    if (evepissed >= 1):
                                                        l "No."
                                                        e "Eh? But I-"
                                                        l "No. Go away."
                                                        e "But I’m-"
                                                        l "NO."
                                                        e "Women are so weird..."
                                                        e "Uh, ok, but still I-"
                                                        jump bschoice_b2
                                                    else:
                                                        l "With what?"
                                                        e "This is going to sound strange, but do you remember those magician weirdos with the hats I was talking to before?"
                                                        l "Yeah, they were pretty memorable. What about them?"
                                                        e "I think they cast a spell on me or something. I keep doing things I don’t want to do and I can’t control myself."
                                                        l "That sounds more like a medical condition, probably brought on by your unhealthy obsession with being average."
                                                        l "It’s probably the unique spirit inside you yearning to be set free."
                                                        e "No way, I murdered that little guy years ago. It has to be a mystical curse or something."
                                                        l "Well, try reading up on them. I overheard the part where they said we need more books on doll mythology or something, so I ordered a few."
                                                        menu:
                                                            "Go read them":
                                                                e "I’ll go check them out right now. Thanks a lot Eve."
                                                                l "No problem."
                                                                jump choice14_books2
                                                            "Ask for cliffnotes":
                                                                jump choice15_notes2
                                                        label choice15_notes2:
                                                            e "You’ve already read them, right? Can you just summarize them for me?"
                                                            l "Eh? I did read them, but I’m working now."
                                                            l "I can’t just-"
                                                            e "Eve, I was probably cursed by those guys. Come on, I don’t have time."
                                                            l "Ugh... Jerk."
                                                            l "Well, for a really short summary..."
                                                            l "There was, like, a branch of alchemists back in the middle ages who thought, since they could turn stone into gold, they should be able to transform dolls into humans somehow and make the perfect person."
                                                            l "But it turned out they couldn’t, so they tried turning people into puppets instead, which sounds like brainwashing."
                                                            e "Oh geez."
                                                            l "It’s all a load of crap, I’ve already put it in the fiction section."
                                                            e "Did it say anything more about the brainwashing part?"
                                                            l "Uh, I think so. It said they figured something out, but they always had to kill the brainwashed guy after a while. Apparently all the power from their hats ran out or something if they let him go."
                                                            
                                                            e "Oh."
                                                            e "Oh crap."
                                                            l "You can read it yourself if you have the time; I don’t think anyone’s going to buy books like that anytime soon."
                                                            e "Yeah, thanks Eve."
                                                            l "... I’ll go back to work, then."
                                                            show eve normal at right with move
                                                            show eve normal at offscreenright with move
                                                            if (knowledge == 0):
                                                                $ knowledge += 1
                                                                e "Oh shit, that sounds dangerously similar to what I’m going through. Except I haven’t died..."
                                                                e "...Yet."
                                                                e "I gotta find those magicians. Maybe they can break the curse early or something."
                                                                e "For now, I’ll-"
                                                                jump bschoice_a2
                                                "Tell her everything is all right":
                                                    e "I am completely fine and not in any trouble at all."
                                                    l "..."
                                                    l "Is that so?"
                                                    e "Yeah, everything is totally average."
                                                    l "..."
                                                    if (evepissed >= 1):
                                                        l "Then go away."
                                                    else:
                                                        l "So you just came here to annoy me in your free time?"
                                                        e "Yeah pretty much"
                                                        l "Go away."
                                                    e "But also, I-"
                                                    jump bschoice_b2
                                                "Confess to her ":
                                                    e "I..."
                                                    e "Eve, I can’t control myself any longer."
                                                    if (evepissed == 3):
                                                        play sound "punch.ogg"
                                                        show eve punch at right
                                                        pause
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done
                                                    elif (evepissed == 1):
                                                        l "..."
                                                    else:
                                                        l "...?!??"
                                                    e "I’ve always enjoyed talking with you..."
                                                    e "You’ve been with me here since day one, and I thought I would be happy with us just being friends..."
                                                    if (evepissed == 1):
                                                        l "..."
                                                    else:
                                                        l ".............."
                                                    e "But lately, you’ve grown to be something more to me. Something important."
                                                    if (evepissed == 1):
                                                        l "..."
                                                    else:
                                                        l "And?"
                                                    menu:
                                                        "Propose to her":
                                                            jump choice16_propose2
                                                        "Ask to go out with her ":
                                                            jump choice16_askout2
                                                        "Ask to borrow some money ":
                                                            jump choice16_money2
                                                        "Tell her it was a joke ":
                                                            jump choice16_joke2
                                                        "Ask her to be your best friend ":
                                                            jump choice16_bf2
                                                    label choice16_propose2:
                                                        if (evepissed >= 1):
                                                            e "WILL YOU MARRY M-"
                                                            play sound "punch.ogg"
                                                            show eve punch at center
                                                            pause
                                                            scene bg death
                                                            stop music
                                                            play music "scary_music.ogg"
                                                            pause
                                                            jump choice0_done
                                                        else:
                                                            e "WILL YOU MARRY ME?"
                                                            l "..."
                                                            l "..."
                                                            l "..."
                                                            l "... No."
                                                            e "OK..."
                                                            e "Kill me now."
                                                            e "Also, I-"
                                                            jump bschoice_b2
                                                    label choice16_askout2:
                                                        e "Will you go out with me?"
                                                        if (evepissed >= 1):
                                                            l "No. Go away."
                                                        elif (evedate == 1):
                                                            l "I already said yes."
                                                            e "Oh, right."
                                                            e "..."
                                                            e "Also, I-"
                                                            jump bschoice_b2
                                                        else:
                                                            l "Sure, I guess."
                                                            e "Sweet."
                                                            l "Not while I’m on duty though..."
                                                            l "We’ll talk later when it’s my day off."
                                                            e "When's that?"
                                                            l "I’ll call you."
                                                            e "Sure thing."
                                                            e "You rock, unknown omnipresent puppeteer wingman dude!"
                                                            $ evedate == 1
                                                            e "Also, Eve, I-"
                                                            jump bschoice_b2
                                                    label choice16_money2:
                                                        e "Can I borrow some cash?"
                                                        l "..."
                                                        e "I wouldn’t ask this from anyone else but you."
                                                        l "..."
                                                        e "Just like 10$, you cheap bit-"
                                                        play sound "punch.ogg"
                                                        show eve punch at center
                                                        pause
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done
                                                    label choice16_joke2:
                                                        e "I‘m just kidding."
                                                        l "..."
                                                        e "LOL the look on your face..."
                                                        if (evepissed <= 1):
                                                            l "Go away, asshole."
                                                            e "Hahaha,"
                                                            e "MAN I’m funny."
                                                            l "Fuck. Off."
                                                            $ evepissed == 3
                                                            e "Oh, also, I-"
                                                            jump bschoice_b2
                                                        else:
                                                            play sound "punch.ogg"
                                                            show eve punch at center
                                                            pause
                                                            scene bg death
                                                            stop music
                                                            play music "scary_music.ogg"
                                                            pause
                                                            jump choice0_done
                                                    label choice16_bf2:
                                                        e "Will you be my best friend?"
                                                        if (evepissed >= 1):
                                                            l "…No."
                                                            e "Aww maaan."
                                                            e "Also, I-"
                                                            jump bschoice_b2
                                                        else:
                                                            l "…What?"
                                                            e "Like right now we’re just friends, right? Can we be best friends?"
                                                            l "…What’s the difference?"
                                                            e "Idk. Actually I don’t think I’m friends with anyone else, so you’re kinda my best friend by default..."
                                                            l "… I hate you."
                                                            e "No you don’t, best friend. Anyway, I-"
                                                            jump bschoice_b2
                                                "Amuse her":
                                                    e "I am the meanest guy around."
                                                    if (evepissed >= 1):
                                                        l "..."
                                                    else:
                                                        l "… Oh really?"
                                                    e "You deny it now? After I’ve been declaring it out loud all my life?"
                                                    if (evepissed == 1):
                                                        l "..."
                                                        l "Oh."
                                                        l "you... mean..."
                                                        l "... as in average."
                                                        l "..."
                                                        e "HA, you smiled."
                                                        l "..."
                                                        e "Come on, cheer up from whatever I did. Even an average guy like me has an upper and lower range."
                                                        l "... Shut up."
                                                        e "You’re smiling again. My batting average is 2 for 2 so far!"
                                                        l "... Heh, you moron."
                                                        e "It's hard to deviate from our average relationship isn’t it?"
                                                        l "I guess so."
                                                        e "Great."
                                                        e "I guess that calmed her down a bit."
                                                        e "Also, Eve, I-"
                                                        jump bschoice_b2
                                                    else:
                                                        l "…Oh, I get it."
                                                        e "Mean as in average."
                                                        e "Mathematics also one of your many areas of expertise then?"
                                                        l "Of course."
                                                        e "Figures. Also, I-"
                                                        jump bschoice_b2
                                        label choice14_books2:
                                            e "Go read some books. It’s a bookstore, after all."
                                            scene bg bookstore2
                                            show bryant normal at left
                                            e "Hmm, what to read?"
                                            label bschoice_c2:
                                                menu:
                                                    "Go back to the entrance":
                                                        e "Eh, I’ll head back to the entrance."
                                                        jump bschoice_a2
                                                    "Read some Shakespeare ":
                                                        jump choice17_shakespeare2
                                                    "Read some cooking recipes ":
                                                        jump choice17_cooking2
                                                    "Read about dwarves abusing quantum mechanics ":
                                                        jump choice17_dwarves2
                                                    "Read up on magicians ":
                                                        jump choice17_magicians2
                                                label choice17_shakespeare2:
                                                    "“To die, to sleep- to sleep, perchance to dream- ay, there’s the rub, for in this sleep of death, what dreams may come…”"
                                                    e "I don’t get it, so was this guy sleepy or emo? And who was he rubbing? Wait no, was someone rubbing him? Is that what he’s on about?"
                                                    e "Overhyped. Probably paid for all those rave reviews. Ugh, next..."
                                                    jump bschoice_c2
                                                label choice17_cooking2:
                                                    "“1: Place water and rice in microwave-safe bowl. If desired, add tub margarine and salt to taste. 2: Cover. Microwave on high for ~5 minutes, or more per serving. 3: Let stand 5 minutes or until water is absorbed. Fluff with fork.”"
                                                    e "Wow, this is a lot better than history. Next..."
                                                    jump bschoice_c2
                                                label choice17_dwarves2:
                                                    "“It is unclear exactly how two (or more) mechanisms talk to each other at a distance without building direct mechanical or electronic channels between them (such as a wire), and given that the Dwarves have not discovered radio technology, it is believed by some that the Dwarves have actually discovered how to implement and control quantum entanglement on a non-quantum scale.”"
                                                    e "...."
                                                    e "Wait, uhhh.."
                                                    e "Um..."
                                                    e "..."
                                                    jump bschoice_c2
                                                label choice17_magicians2:
                                                    if (knowledge == 1):
                                                        e "“This must be the book eve was talking about. I’ll skim through it”"
                                                    e "“After successfully perfecting the technique of altering base substances to higher forms (Commonly remembered for the stone to gold example), the alchemists sought to elevate the human form instead.”"
                                                    e "“This proved too difficult a feat with their limited resources, and internal conflicts lead to a schism; The alchemists continued into Europe to profit off their current knowledge, but a small number obsessed with creating a perfect form diverged into the new continent, calling themselves ‘Magicians’ instead”"
                                                    e "“This sect explored the possible connections between the human form and that of the perfect template, puppets, and if their mystic powers could somehow forge a stable connection between the two”"
                                                    e "Oh man, this must be it. Lets see, anything about magic spells?"
                                                    e "“... spells were very taxing, and the subjects that were often subject to forces outside of their control, causing them to wander off with the mages power still held within them. To solve this problem, most common rituals included a low costing lethal, but reversible curse that would cause the subject to die after %(daysleft)d days.”"
                                                    e "“The effort required to reverse the curse became inefficient as the number of subjects for testing rose dramatically; it became second nature to simply have domination spells kill off the subject after a week or so.”"
                                                    e "Oh no. Ohhh nooooooo..."
                                                    e "But, it said it was reversible, do I have a chance?"
                                                    e "“… reversing domination is a long and complex process, requiring counterchants lasting at least 3-4 lengths longer than the original hyme, also including a mirror of recursive scrying,”"
                                                    e "“... underneath the full moon... requires at least 500gp worth of components... must rest for 1-4 days afterwards...”"
                                                    e "Cmon, I’m trying to save my life here, I don’t need this nerd crap."
                                                    e "“...or alternatively collect the focus of power for each person involved in the original casting, usually an article of clothing or magical item that holds deep symbolism / importance to the owner, and adorn them yourself.”"
                                                    e "there we go... that means..."
                                                    e "I just have to collect their ‘power focuses’, which is... uh.."
                                                    e "It has to be their hats! That’s it! I collect their hats before this time limit is up, and I won’t die from the curse!"
                                                    $ knowledge == 2
                                                    scene bg bookstore1
                                                    show bryant normal at left
                                                    e "But now I’ve got to find them, and I don’t have any leads."
                                                    e "Hmm, I’m not really sure what I should do next."
                                                    e "I guess I’ll-"
                                                    jump bschoice_a2
                                        label choice14_work2:
                                            e "Go work some overtime."
                                            e "Can’t have enough extra cash, I suppose."
                                            show citizen normal at offscreenright with move
                                            show citizen normal at right with move
                                            c "Excuse me, do you work here?"
                                            e "Yes, I do."
                                            c "Great. Can you direct me to the history section?"
                                            scene black
                                            "*Many boring hours later*"
                                            scene bg bookstore1
                                            show bryant normal at center
                                            e "Feels just like the good old average days again."
                                            e "Except the rates on my time off are lower, ugh."
                                            e "Still, 100$ is 100$"
                                            $ money += 100
                                            e "Everyone else already went home. No choice but to head back home."
                                            jump apartmentn2
                                        label choice14_fire2:
                                            show policeman normal at offscreenright with move
                                            show policeman normal at right with move
                                            e "Just set the whole bookstore on fire, I guess."
                                            p "ARE you now?"
                                            e "I guess I a-"
                                            e "..."
                                            e "Why is there a policeman in the bookstore?"
                                            p "Are policemen not allowed to buy books?"
                                            e "..."
                                            p "You’re under arrest."
                                            e "On what charges?"
                                            p "Premeditated arson, but mostly blatant racism."
                                            e "Wondering why a cop is eavesdropping on me in the middle of a bookstore is blatant racism?"
                                            p "“Why would a cop be in a bookstore? I thought pigs couldn’t read.”"
                                            e "I didn’t say that!"
                                            p "That’s what it sounded like to me. It’s always “What is a policeman doing here? Shouldn’t he be out giving parking tickets like the rest of his little buddies? Why are you in my house?”"
                                            p "Well how about now? I caught an arsonist in the act!"
                                            menu:
                                                "Surrender quietly":
                                                    e "Ok, you caught me. Now what?"
                                                    p "I’ll just bring you to the station, and you’ll have to watch a presentation to learn about the importance of being a better member of the community."
                                                    e "That’s it? I was going to burn down this Bookstore for no discernable reason."
                                                    p "The presentation is about 7 hours long. If you survive, the community spirit will be burned into your skull, and whatever’s left of you is free to go."
                                                    e "Oh god... Please no..."
                                                    scene black
                                                    "*7 hours later*"
                                                    jump apartmentn2
                                                "Deny the charges ":
                                                    jump choice18_deny2
                                                "Kick him and run for it ":
                                                    jump choice18_kick2
                                            label choice18_deny2:
                                                e "But I didn’t actually do anything, I just said I was going to."
                                                p "You think words can’t hurt people? Cops have feelings too you know. And they can read. I read a lot."
                                                e "Yes, I’m sure, but I’m just saying I didn’t actually do anything illegal enough to be arrested."
                                                p "Don’t change the subject, racist."
                                                p "And quit going on about that."
                                                p "..."
                                                p "I’m watching you."
                                                e "You were before, too."
                                                show policeman normal at right with move
                                                show policeman normal at offscreenright with move
                                                e "Hmph. Now then, I’ll-"
                                                jump bschoice_a2
                                            label choice18_kick2:
                                                e "Uh, think fast!"
                                                p "Are you implying cops can’t thin-OW"
                                                show bryant normal at left with move
                                                show bryant normal at offscreenleft with move
                                                pause
                                                scene bg citysidewalk
                                                show bryant normal at right
                                                e "I think I lost him!"
                                                e "Wait, I just attempted to burn down the place I work at and then assaulted an officer to escape arrest!"
                                                e "I’m gonna have to go on an average spree after this curse thing gets sorted out..."
                                                jump map2
                                                

                                                    
                                                       

                                            
                                            
                                            
                                            
                                            
                                            
                                                
                                            
                                            
                                                           
                                                        
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                            
                                                        
                                                        
                                                            
                                                        
                                                    
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                    
                                                       
                                                    
                                                
                                                                
                                                            
                                                        
                                                        
                                                        
                                                        
                                                    
                                                    
                                                    
                                                
                                            
                                            
                                            
                                    jump map2
                                elif result == "alley":
                                    scene bg alley
                                    show bryant normal
                                    e "Oh! What am I doing here?"
                                    e "I should probably get out before I get raped!"
                                    jump map2
                                elif result == "apartment":
                                    label apartmentn2:
                                        scene bg apartmentnight
                                        show bryant normal at center
                                        if (hat == 0) and (knowledge == 0):
                                            e "(Well, I’m still no further to finding out about this whole curse thing.)"
                                            e "(Maybe I’ll get to it tomorrow, then.)"
                                            e "Asking Eve about those weirdos seems like my only option at this point.)"
                                        elif (hat == 0) and (knowledge == 1):
                                            e "(Now I know that it’s really a curse they put on me, but I still don’t know much about it.)"
                                            e "(Maybe I should have read the books)"
                                            e "(Or I could just find a magician and ask him to undo it, I guess)"
                                        elif (hat == 0) and (knowledge == 2):
                                            e "(Another day wasted, and I’ve still got to find those magicians before it’s too late.)"
                                            e "(I’m not even sure where they all are at this point)"
                                            e "(I gotta hurry up.)"
                                        elif (hat == 1):
                                            e "(I’ve got one hat now, but I still need to get the other three.)"
                                            e "(That first magician said one of his friends liked food or something, didn’t he?)"
                                            e "(The only place for food I can think of is that burger store downtown.)"
                                            e "(I’ll get to it tomorrow, I hope.)"
                                        elif (hat == 2):
                                            e "(I’ve got two hats now, but I still need two more to undo the curse.)"
                                            e "(I’ll need to get them pretty quick)"
                                            e "(that time limit is coming soon.)"
                                        elif (hat == 3):
                                            e "(Only one more hat to go, totally final battle stuff goin on. )"
                                            e "(I can hardly wait)"
                                            e "(I’ll finally be able to go back to being average again.)"
                                        scene black
                                        "Tap to continue..."
                                        $ day += 1
                                        $ daysleft -= 1
                                        if (daysleft <= 0):
                                            play sound "spell.ogg"
                                            scene bg death
                                            stop music
                                            play music "scary_music.ogg"
                                            pause
                                            "Bryant ran out of time."
                                            jump choice0_done
                                        else:
                                            scene bg apartmentday
                                            show bryant normal
                                            e "Yawn ..."
                                            e "Looks like another"
                                            e "disgustingly erratic day, with this curse controlling my every move."
                                            e "Oh well, time to find a way to break it!"
                                        jump map2
                                elif result == "bank":
                                    scene bg bank
                                    show bryant normal at left
                                    show bankteller normal at right
                                    e "Wait, the bank? What do I need at the bank?"
                                    bt "Can I help you, sir?"
                                    label bankchoice2:
                                        menu:
                                            "Leave the bank":
                                                e "Nope, thanks for the offer."
                                                bt "Enjoy your day then."
                                                jump map2
                                            "Start a conversation ":
                                                jump choice23_conv2
                                            "Make a deposit / withdraw ":
                                                jump choice23_make2
                                            "Check your balance ":
                                                jump choice23_balance2
                                            "Rob the bank ":
                                                jump choice23_rob2
                                        label choice23_conv2:
                                            e "Nice weather we’re having, isn’t it?"
                                            bt "Uh, yes, yes it is."
                                            e "Not that I can tell, I haven’t looked upwards in a while now."
                                            e "That and most people don’t seem to have feet, for some odd reason. And it looks like everyone is talking without moving their lips."
                                            bt "Excuse me, but this seems more like a medical condition on your part, sir."
                                            e "I’d go to the hospital, but it’s not one of the options on that map thing I keep seeing. I doubt they could cure the weirdness a group of magicians cast on me a few days ago anyways."
                                            bt "Uh... um... anything more, banking related, I could help you with sir?"
                                            jump bankchoice2
                                        label choice23_make2:
                                            e "I’d like to access my account, please."
                                            bt "Certainly, what for?"
                                            menu:
                                                "Deposit all your money":
                                                    jump choice24_depa2
                                                "Deposit 100$":
                                                    jump choice24_depb2
                                                "Do nothing ":
                                                    jump choice24_none2
                                                "Withdraw 100$ ":
                                                    jump choice24_witha2
                                                "Withdraw all your money ":
                                                    jump choice24_withb2
                                            label choice24_depa2:
                                                e "I’d like to deposit all my money."
                                                if (money == 0):
                                                    bt "Erm, what money, sir?"
                                                    e "Oh, right. Nevermind."
                                                    bt "Uh, anything else I can help you with?"
                                                    jump bankchoice2
                                                else:
                                                    $ bank += money
                                                    $ money = 0
                                                    bt "Right away. You now have a total of %(bank)d in your savings."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice2
                                            label choice24_depb2:
                                                e "I’d like to deposit 100$"
                                                if (money == 0):
                                                    bt "Erm, what money, sir?"
                                                    e "Oh, right. Nevermind."
                                                    bt "Uh, anything else I can help you with?"
                                                    jump bankchoice2
                                                else:
                                                    $ money -= 100
                                                    $ bank += 100
                                                    bt "Right away. You now have a total of  %(bank)d in your savings."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice2
                                            label choice24_none2:
                                                e "Nevermind."
                                                bt "Oh, ok then…"
                                                bt "Anything else?"
                                                jump bankchoice2
                                            label choice24_witha2:
                                                e "I’d like to withdraw 100$"
                                                if (bank < 100):
                                                    bt "It seems you don’t have 100$ in your account, sir."
                                                    e "Darn it. Nevermind, then..."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice2
                                                else:
                                                    $ money += 100
                                                    $ bank -= 100
                                                    bt "Right away. You now have a total of %(bank)d in your savings."
                                                    bt "Anything else I can help you with?"
                                                    jump bankchoice2
                                            label choice24_withb2:
                                                e "I’d like to withdraw all my money."
                                                if (bank == 0):
                                                    bt "It seems your account is completely empty, sir."
                                                    e "Really? That sucks."
                                                    bt "Indeed. Anything else I can help you with?"
                                                    jump bankchoice2
                                                else:
                                                    $ money += bank
                                                    $ bank = 0
                                                    bt "Right away. You now have no savings."
                                                    e "Yolo."
                                                    bt "Right..."
                                                    bt "...anything else I can help you with?"
                                                    jump bankchoice2
                                                
                                        label choice23_balance2:
                                            e "I’d like to check my account balance."
                                            bt "Lets see, Bryant Day correct? You have %(bank)d dollars saved up here."
                                            e "(and I have %(money)d on hand)"
                                            bt "Anything else I can help you with today?"
                                            jump bankchoice2
                                        label choice23_rob2:
                                            e "I’d like to make a withdraw, actually."
                                            bt "How much, sir?"
                                            show bryant gun at left
                                            e "THE ENTIRE GODDAM BANK. THIS IS A ROBBERY."
                                            bt "Oh god. Sir, please calm down."
                                            e "I’LL CALM DOWN WHEN YOU START HANDING OVER THE CASH!"
                                            bt "Sir, you’re trying to rob a bank in broad daylight with no mask, just calm down and give yourse- "
                                            e "I’M CALM RIGHT NOW. IF YOU DON’T WANT TO SEE ME ANGRY, START HANDING ME THE MONEY NOW."
                                            e "(OhmygodohmygodohmygodwhatamIdoing)"
                                            e "(WHERE DID THIS GUN EVEN COME FROM DID I BRING IT WITH ME AND NOT EVEN NOTICE WHAT THE HELL!)"
                                            p "This is the police, we have you surrounded."
                                            p "At least on this side."
                                            p "Release the hostages and lay down your weapon, NOW."
                                            e "YOU DON’T CONTROL ME, PIGS I’LL-"
                                            menu:
                                                "Surrender":
                                                    jump choice25_surrender2
                                                "Waste a hostage ":
                                                    jump choice25_hostage2
                                                "Go down in a blaze of glory ":
                                                    jump choice25_blaze2
                                                "Make a deposit":
                                                    jump choice25_deposit2
                                            label choice25_surrender2:
                                                p "Surrender quietly."
                                                p "..."
                                                p "Oh, geez, really? That usually doesn’t work."
                                                p "I mean wow, finally, someone who listens to a cop. I’ve been yelling at people for years, and they all just ignore me."
                                                p "This is great. And I’ll probably get the rest of the day off too."
                                                p "Hell, you’ve learned your lesson, right?"
                                                e "Uh, yeah, totally."
                                                p "You’re not gonna do it again, right?"
                                                e "...Maybe."
                                                p "Tell ya what..."
                                                p "Just go home, get a good nights sleep, think about what you did, and I’ll let you off the hook. OK?"
                                                e "Uh... Yeah, sure."
                                                p "Good man. And a good LISTENER, too. You take care now."
                                                e "Right...see you then."
                                                
                                                jump apartmentn2
                                            label choice25_hostage2:
                                                p "PROVE IT."
                                                bt "NO, PLEASE, I HAVE A WIFE AND KIDS. MERCY."
                                                bt "HE'S IGNORING THE HOSTAGE AFTER BEING ASKED SO POLITELY. TAKE HIM DOWN!"
                                                play music "gunshot.wav"
                                                show policeman shooting at right
                                                pause
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                            label choice25_blaze2:
                                                e "I'M GONNA TAKE YOU ALL DOWN WITH ME."
                                                bt "He’s lost it! Take him down!"
                                                play music "gunshot.wav"
                                                show policeman shooting at right
                                                pause
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                            label choice25_deposit2:
                                                show bryant normal at left
                                                e "Make a deposit, please."
                                                bt "Wait, what?"
                                                e "Oh, wait, sorry, are you closed now?"
                                                bt "HE’S LOWERED HIS GUARD. TAKE HIM DOWN."
                                                play music "gunshot.wav"
                                                show policeman shooting at right
                                                pause
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                                
                                                
                                                
                                                
                                                
                                                
                                                        
                                                
                                                                    
                                                                       
                                    
                                    
                                    jump map2
                                    
                                    
                                    
                                elif result == "burgerstore":
                                    scene bg burgerstore
                                    show bryant normal at left
                                    show burgerdude normal at right
                                    e "“The burger store, always good to grab a bite to eat when you’re trying to break some freaky mind control curse.”"
                                    b "*sigh* Hello, valued customer, may I take your order?"
                                    label burgerstorea_2:
                                        menu:
                                            "Leave":
                                                b "Thank you for your patronage… *sigh*"
                                                jump map2
                                            "Order some burgers":
                                                jump choice19_burger2
                                            "Order some tacos ":
                                                jump choice19_tacos2
                                            "Ask about magicians ":
                                                jump choice19_ask2
                                            "Rob the place ":
                                                jump choice19_rob2
                                        label choice19_burger2:
                                            if (money == 0):
                                                e "I’d like a burger, please."
                                                b "Yes, “sir”. Here you are."
                                                e "Oh, actually it looks like I don’t have any money on me, sorry."
                                                b "*Sigh* I guess we’ll have to throw it out then."
                                                b "Disgusting crap isn’t fit to be eaten anyway. mumble mumble."
                                                e "What was that?"
                                                b "Anything else, sir?"
                                                jump burgerstorea_2
                                            $ money -= 5
                                            if (burgers == 0):
                                                $ burgers = 1
                                                e "I’d like a burger, please."
                                                b "Yes, “sir”. Here you are."
                                                e "Thanks! *nomnomnom*"
                                                b "Anything else for you today, “sir”?"
                                                jump burgerstorea_2
                                            elif (burgers == 1):
                                                $ burgers = 2
                                                e "I’ll have another burger. A few more, actually."
                                                b "Right away, “sir”."
                                                e "*nomnomnom* Mmm, sooo many burgers. I don’t think I can handle another bite."
                                                b "You probably could, you fatass."
                                                e "What?"
                                                b "I asked if you were going to order anything else, “sir”?"
                                                jump burgerstorea_2
                                            else:
                                                $ money -= 100
                                                $ burger = 0
                                                e "I’ll have a few more burgers, actually."
                                                b "How many?"
                                                e "Hmmm…"
                                                e "How many do you have?"
                                                scene black
                                                "*hours later*"
                                                scene bg burgerstore
                                                show bryant angry at left
                                                e "Ughhh... uff... URP."
                                                e "What... what happened?"
                                                b "You were inhaling burgers till you passed out, “sir”."
                                                e "What? How long was I out?"
                                                b "A couple hours, its 11:00 now."
                                                e "11:00?!? I wasted my entire day here!"
                                                e "Wait, I passed out for multiple hours and you just left me here? No ambulance or anything?"
                                                b "They don’t pay me enough to care."
                                                e "... No one else cared?"
                                                b "You think anyone else comes to this place?"
                                                e "Point taken... Ugh... I’m still nauseous."
                                                b "That makes two of us, sir."
                                                e "... I’m leaving."
                                                b "Thank you, come again."
                                                jump apartmentn2
                                        label choice19_tacos2:
                                            e "I’d like a taco, please."
                                            b "Sir, this is a burger store."
                                            e "Don’t you have some tacos in storage, just in case or something?"
                                            b "No."
                                            e "Could you, like, form burger meat into the filling and make the bun in a taco shape?"
                                            b "No."
                                            e "Uh, could you order tacos for delivery and have me pay you for them?"
                                            b "No."
                                            e "What can you do?"
                                            b "Tolerate morons like you while I work for minimum wage."
                                            e "Barely."
                                            b "Will that be all, valued customer?"
                                            jump burgerstorea_2
                                        label choice19_ask2:
                                            e "Do you happen to know anything about a group of hat-wearing wizards obsessed with puppets that shout loudly about anything that remotely annoys them?"
                                            if (hat == 0):
                                                b "Sir, are you going to order some burgers or not?"
                                                jump burgerstorea_2
                                            elif (hat > 1):
                                                b "Not anymore."
                                                jump burgerstorea_2
                                            else:
                                                b "Oh, you know him?"
                                                e "\"Him\"? You mean you know about one?"
                                                b "He’s in the playpen area, and eats more than the usual fatasses, but doesn’t pay for meals, and keeps yammering about dolls and other stuff."
                                                e "Really?!? I’ll go talk with him."
                                                jump playpen2
                                        label choice19_rob2:
                                            e "I’d like to order..."
                                            e "All the money in your register."
                                            b "Sir, that’s not for sale."
                                            e "Uh... I’m robbing you."
                                            b "Sir, robbery is illegal."
                                            e "I know it is, but I’m doing it anyway. Now give me the money or I’ll threaten you a second time."
                                            b "Sir, being a devout believer in reincarnation, the threat of physical violence doesn’t scare me."
                                            b "That, and I’ve stood here for 5 years having to watch disgusting fatasses chug burgers for minimum wage and no hope of advancement."
                                            b "If you don’t do it, I’ll get around to it eventually."
                                            e "Wow, you’re really depressing."
                                            b "I know, right?"
                                            b "So are you gonna order some shit or what?"
                                            jump burgerstorea_2
                                        label playpen2:
                                            scene bg burgerstoreplaypen
                                            show magicianblue normal at right
                                            show bryant normal at left
                                            show forcefield normal at right
                                            m3 "*Munch, snarf, gobble*"
                                            e "Hey you! Magician!"
                                            m3 "*Crunch* Eh? What do you want, mortal?"
                                            e "You and your buddies cursed me, remember?"
                                            m3 "..."
                                            m3 "Oh, that’s right... I remember you. Curse of the puppet right?"
                                            e "Yeah, and it turns out you forgot about how the curse will kill me if I don’t remove it."
                                            m3 "..."
                                            if(difficulty == 0):
                                                m3 "Oh, that’s right, I remember that, you die after 7 days with it, right?"
                                            else:
                                                m3 "Oh, that’s right, I remember that, you die after 5 days with it, right?"
                                            m3 "..."
                                            e "So hand over the hat!"
                                            m3 "What? No."
                                            e "But I’m going to die without it!"
                                            m3 "So? "
                                            e "Eh?"
                                            m3 "There are like 6 billion of you running around the place. Get over it."
                                            e "Wait, you can’t just ignore me when I’m about to die!"
                                            m3 "*Chew* Watch me, mortal."
                                            label playpenchoice2:
                                                menu:
                                                    "Go back to the register":
                                                        jump choice20_register2
                                                    "Ask for the hat":
                                                        jump choice20_hat2
                                                    "Ask about him ":
                                                        jump choice20_ask2
                                                    "Try reverse psychology ":
                                                        jump choice20_psychology2
                                                    "Punch him in the face ":
                                                        jump choice20_punch2
                                                label choice20_register2:
                                                    e "Fine, I’m going back to the register."
                                                    m3 "Whaaatever. *Chomp, munch*"
                                                    scene bg burgerstore
                                                    show bryant normal at offscreenleft
                                                    show burgerdude normal at right
                                                    show bryant normal at left with move
                                                    b "Is he going to pay now?"
                                                    e "Nope, don’t think so."
                                                    b "I’d tell him to get out, but I really don’t care that much."
                                                    e "Apparently."
                                                    e "..."
                                                    jump burgerstorea_2
                                                label choice20_hat2:
                                                    e "Really, though, can I have your hat?"
                                                    m3 "Nope. *gobble*"
                                                    e "Do I need to pass a test first? Earn it somehow?"
                                                    m3 "No. Go away. *Buuuurp*"
                                                    e "Come on, I gotta get it somehow."
                                                    m3 "Even if I was willing, you couldn’t. I accidentally cast a force field between me and the outside world, so you can’t even come near me if you tried."
                                                    e "What?!? Then how do you keep ordering all those burgers?!?"
                                                    m3 "I ordered all these beforehand, THEN I made the forcefield."
                                                    m3 "Oh, I mean, made it on accident."
                                                    e "Wait, you ordered all those burgers and just made a forcefield around yourself to eat them in peace?"
                                                    m3 "Doesn’t work that well, apparently. I can still hear your whiny little mortal complaints. *crunch, smack*"
                                                    e "So then how are you getting air in there?"
                                                    m3 "There’s actually an entrance over there: I bewitched the playpen tunnels to become a labyrinth that only a masterful wizard could solve, and air can pass through."
                                                    e "So, I could possibly go in there and get your hat if I passed through your labyrinth?"
                                                    m3 "*Chew, snarf* Fine, mortal. Pass my maze and I’ll give you my hat. If and when you can’t, go run away like a good mortal."
                                                    
                                                    label playpenchoices32:
                                                        menu:
                                                            "Run away like a good mortal":
                                                                e "Nevermind, I won’t try it."
                                                                m3 "...Suit yourself.  *Eating noises*"
                                                                jump playpenchoice2
                                                            "Try the maze ":
                                                                e "Fine then, I’ll try your maze."
                                                                m3 "*Buuurp* Dinner with a show, this shall be entertaining."
                                                                "Use the arrow keys to move in the maze. Reach the exit before time expires or you’ll be expelled back to the entrance again."
                                                                python:
                                                                    renpy.free_memory()
                                                                    
                                                                    if (difficulty == 0):
                                                                        success = maze.main()
                                                                    else:
                                                                        success = mazedifficult.main()
                
                                                                if success == 1:
                                                                    show bryant happy at right
                                                                    show forcefield normal at right
                                                                    e "HA! I got past your stupid maze! Now we meet face to face."
                                                                    m3 "Oh. Well how about that."
                                                                    e "Now give me your hat!"
                                                                    m3 "... Naw."
                                                                    e "But you said-"
                                                                    m3 "I crossed my fingers."
                                                                    e "... You were eating hamburgers while promising."
                                                                    m3 "Who cares, you’re just a mortal. Get over it."
                                                                    menu:
                                                                        "Demand the hat":
                                                                            jump choice21_hat2
                                                                        "Give up and leave ":
                                                                            jump choice21_leave2
                                                                        "Punch him in the face ":
                                                                            jump choice21_punch2
                                                                    label choice21_hat2:
                                                                        e "No! I passed your maze, now give me your hat! A promise is a promise."
                                                                        m3 "*Chew* Promises with wizards are different. We say one thing, but we mean another thing of equal value."
                                                                        e "Eh? So what are you offering me instead?"
                                                                        m3 "Learning a one way teleport spell."
                                                                        e "... That actually sounds pretty useful."
                                                                        m3 "*Gobble* Indeed it is. Watch closely..."
                                                                        show magicianblue casting at right
                                                                        play sound "spell.ogg"
                                                                        pause 2.0
                                                                        hide bryant with dissolve
                                                                        show bryant normal at left with dissolve
                                                                        show magicianblue normal at right
                                                                        e "Wait, I’m just outside the forcefield again."
                                                                        m3 "Yeah, did you see me casting it? I don’t normally give lessons like that so cheap."
                                                                        e "Hey, you can’t get rid of me that easily!"
                                                                        m3 "Just did. *Gulp*"
                                                                        e "Asshole fatty magician grumble grumble..."
                                                                        jump playpenchoice2
                                                                    label choice21_leave2:
                                                                        e "Fine, I give up."
                                                                        m3 "... So easily? Mortals are such fickle creatures. *Chew*"
                                                                        m3 "As you wish."
                                                                        hide bryant with dissolve
                                                                        show bryant normal at left with dissolve
                                                                        e "Wait, you can teleport me?"
                                                                        m3 "Apparantly."
                                                                        e "Couldn’t you have just teleported me inside, rather than watch me rush through a crazy mystical playpen maze?"
                                                                        m3 "But that was the best part! *Gulp*"
                                                                        e "... Asshole fatty magician grumble grumble…"
                                                                        jump playpenchoice2
                                                                    label choice21_punch2:
                                                                        play sound "punch.ogg"
                                                                        show bryant punch at center
                                                                        m3 "*Belch* OW! Owwww..."
                                                                        show bryant normal at center
                                                                        e "No more mystical forcefield, eh promise breaker?"
                                                                        
                                                                        m3 "Ugh... Simple barbarian, you trifle with powers beyon-"
                                                                        play sound "punch.ogg"
                                                                        show bryant punch at center
                                                                        m3 "OWW! Stop that!"
                                                                        show bryant normal at center
                                                                        e "Give up the hat, and this will all be over soon, spellslinger."
                                                                        play sound "punch.ogg"
                                                                        show bryant punch at center
                                                                        m3 "OWWowowow. Fine, fine you annoying insect, take it, whatever."
                                                                        hide magicianblue
                                                                        show magician normal at right
                                                                        show bryant normal at center
                                                                        $ hat += 1
                                                                        e "Yes! Only two more to go! Thank you, brute force!"
                                                                        m3 "Hmph. Disgusting creature, *Chomp, slurp, gobble*"
                                                                        e "You’re staying here, I assume, but where are your other friends?"
                                                                        m3 "I’m not sure, I stayed here to sample these delicacies and the others went their own way. The one in the yellow hat frequents that one place with those militant thugs. That’s where I would search for him."
                                                                        e "Wait, you don’t know the other's names either?"
                                                                        m3 "It never came up, really, so it doesn’t matter."
                                                                        m3 "For your information, I’ll be leaving this place as well, as much as I hate to part with these wonderful delicacies."
                                                                        e "What, you finally learned that your force field isn’t impenetrable, so you’re running away?"
                                                                        m3 "..."
                                                                        m3 "... nooo..."
                                                                        m3 "...*Chomp*"
                                                                        e "Whatever. As long as I know the other hats are around here somewhere, I still have a chance to save myself before the lethal curse activates!"
                                                                        m3 "Yeah, you go do that. *burp*"
                                                                        scene bg burgerstore
                                                                        show bryant normal at offscreenleft
                                                                        show burgerdude normal at right
                                                                        show bryant normal at left with move
                                                                        e "I talked with him, and he said he was leaving soon."
                                                                        b "Good. The less people I have to interact with around here, the better."
                                                                        b "..."
                                                                        b "Have a good night, “sir”."
                                                                        jump apartmentn2
                                                                elif success == 0:
                                                                    e "Aww, it threw me back here."
                                                                    m3 "You weren’t fast enough, mortal. Completely expected."
                                                                    m3 "This is a labyrinth set to the difficulty of wizards."
                                                                    m3 "It's obvious a mortal would have no chance getting past it."
                                                                    e "Wouldn’t a wizard just teleport to the end?"
                                                                    m3 "... That’s actually the challenge."
                                                                    m3 "..."
                                                                    m3 "... *Chomp*"
                                                                    jump playpenchoices32
                                                                else:
                                                                    e "Nobody likes a quitter..."
                                                                    $ renpy.quit()
                                                label choice20_ask2:
                                                    e "So what does eating a boat-load of burgers have to do with wizardry again?"
                                                    m3 "*Nibble, munch* Foolish mortal... Trying to mock me... "
                                                    m3 "Puppeteering encompasses everything to do on the mortal planes, to some lesser or greater extent, and the desire for exquisite sustenance is no exception. "
                                                    m3 "We’ve had to fast for days while chanting complex spells, and even then only had elixirs and magic beans to survive on after."
                                                    m3 "But this holy mineral you call “Hamburgers” is a culinary breakthrough that earns you the slightest respect in my eyes. Feel honored, mortal."
                                                    e "What, finally realized you prefer eating burgers to playing with dolls?"
                                                    m3 "... I'm getting there. *Chomp*"
                                                    jump playpenchoice2
                                                label choice20_psychology2:
                                                    e "Ugh... What a pathetic wizard."
                                                    m3 "*Gobble, slurp*"
                                                    e "Your friend back at the police station realized he made a mistake, and was willing to throw away his pride and do the right thing."
                                                    m3 "*Chew, crunch, smack*"
                                                    e "Um... I guess he didn’t really throw away his pride..."
                                                    e "He knew he was doing the right thing by giving me his hat, so he actually felt better as a person AND a magician after the whole thing."
                                                    e "... Besides, the hat looks bad on you anyway. Blue isn’t really your color, doesn’t go with your wizard robes at all. A natural hatless look would suit you better."
                                                    m3 "*Bite, crunch, slurp*"
                                                    e "Oh come on, you can’t “slurp” a burger, you’re not even trying."
                                                    m3 "Shhh... I’m trying to remember how to cast silencing spells."
                                                    jump playpenchoice2
                                                label choice20_punch2:
                                                    e "Let's try some ”punch in the face” diplomacy, then."
                                                    show forcefield normal at right
                                                    show bryant punch at left
                                                    play sound "punch.ogg"
                                                    e "OW, that shocked me!"
                                                    show bryant normal at left
                                                    m3 "*Chomp* Yeah... Forcefields tend to do that."
                                                    e "Well turn it off so I can punch you in the face."
                                                    m3 "..."
                                                    m3 "NO."
                                                    jump playpenchoice2
                                                    
                                                    
            
            
    
    
                                                            
                                                               
                                                            
                                                        
                                                    
                

                                                    
                                                
                                            
                                            
                                                
                                                
                                                
                                                
                                                
                                                
                                            
                                        
                                            
                                            
                                    jump map2
                                elif result == "cemetary":
                                    stop music
                                    play music "scary_music.ogg"
                                    scene bg graveyardday
                                    show bryant normal at left
                                    if (hat == 3):
                                        e "(It’s the cemetery. Yellow hat said the last guy would be here.)"
                                        play sound "spell.ogg"
                                        e "(Eh? What’s that sound?)"
                                        e "(Must be some sort of spell or something, I don’t know.)"
                                        e "(Nowhere else to go but forward, then)"
                                        label cemetarychoiceh3_2:
                                            menu:
                                                "Head towards the noise ":
                                                    jump choice26_crypt2
                                                "Sing louder than the noise ":
                                                    jump choice26_loud2
                                                "Tell the noise to shut up ":
                                                    jump choice26_shutup2
                                                "Run away":
                                                    e "(Or, maybe I need to do something else first, I guess)"
                                                    stop music
                                                    play music "main.ogg"
                                                    jump map2
                                            label choice26_loud2:
                                                e "(THE WHEELS ON THE BUS GO ROUND AND ROUND)"
                                                e "...."
                                                e "AND SHES BUUUUYYYYING A STAIRWAY, TO HEAVEN."
                                                e "..."
                                                e "OPPA GANGNAM STYLE !! Wait, what are the rest of the lyrics?"
                                                e "...."
                                                e "(Whatever the hell I was trying to do just now obviously isn’t working)"
                                                jump cemetarychoiceh3_2
                                            label choice26_shutup2:
                                                e "HEY! KEEP IT DOWN! SOME OF US ARE TRYING TO SLEEP!!!"
                                                e "YEAH, SLEEP NOW, AROUND THE MIDDLE OF THE DAY."
                                                e "I KNOW IT SOUNDS STRANGE, BUT YOU PROBABLY SHOULDN’T HAVE THE VOLUME UP SO HIGH ANYWAYS."
                                                e "..."
                                                e "I guess they can’t hear me, or they just don’t care."
                                                jump cemetarychoiceh3_2
                                            label choice26_crypt2:
                                                e "(The sounds are all coming from...)"
                                                e "(This room?)"
                                                scene bg crypt
                                                show magicianred normal at right
                                                show bryant normal at left
                                                m "Oh? Yes, hello mortal, nice of you to join me."
                                                m "Not really. Wipe your feet before coming in, too."
                                                e "Oh, sure, sorry. And what’s with the music?"
                                                m "Ancient incantations far beyond the scope of your relatively limited comprehension, or likely anyone overly familiar with this plane of existence. Calling it “music” is a misnomer."
                                                e "Yeah, yeah, I’ve heard enough magic nerd crap for a life time"
                                                e "Speaking of which, hand over the hat so I can break this curse already"
                                                m "I’m afraid I won’t be swayed as easily as my brethren, mortal."
                                                e "What? Are you the omnipotent wizard demon I have to have an epic duel with now?"
                                                m "No, even worse. I’m the only one actually aware of the curse on you!"
                                                e "Eh? They knew about it, I even reminded them about the lethal part."
                                                m "Yes, but need I remind YOU what we all deemed the “lethal part”?"
                                                e "Uh, a “minor” side effect?"
                                                m "Exactly. The curse of the puppet"
                                                m "one of the few ways for a living being to feel like a puppet, with someone else controlling the strings."
                                                m "Imagine: a stranger with no emotional or physical ties to you is suddenly granted control over your every move with no threat of retribution."
                                                m "Imagine the atrocities they would have you commit, the unspeakable acts they could force you to do for nothing else than their own petty amusement."
                                                m "Every second there is a risk of some new erratic action."
                                                m "Every day there is a chance that they break you out of mere boredom, until you realize the rest of your pathetic, meaningless life is never going to be lived out the way you wanted."
                                                m "But you don’t have to imagine, do you?"
                                                m "You’ve experienced it yourself, the feeling of helpless, abject terror of not being in control of your own actions."
                                                m "I feel that you’re no different than when we first met."
                                                m "The curse, besides the unintentional lethality, was meant to teach you what it’s like, the mere basest of feelings, to have someone else pulling the strings."
                                                m "It should make you feel at your very core, the awe inspiring connection between puppet and puppeteer that we strive among all else to comprehend."
                                                m "I am guessing that you haven’t learned anything, have you mortal?"
                                                e "Whoa, well, I mean um, when you put it that way…"
                                                e "At first I just wanted to get rid of the puppeteer part. Does that count?"
                                                m "I thought not. I KNEW not."
                                                m "Which is why, mortal, I offer you my hat."
                                                e "…What?"
                                                m "Yes, come take it. Consider it your final test"
                                                m "the others had their own for you, in various forms, correct?"
                                                e "..."
                                                m "But on your way, be sure not to step on that pressure plate to your right!"
                                                e "Eh?"
                                                m "Yes, that one. It’s linked to an explosive rune that would certainly be lethal for whomever stepped on it."
                                                m "Pay it no heed, mortal. Just step over here."
                                                menu:
                                                    "Step on the trap":
                                                        e "You mean THIS pressure pla-"
                                                        play sound "explosion.ogg"
                                                        hide bryant
                                                        show explosion normal at left
                                                        m "“…Yes, that one"
                                                        m "I guess it doesn’t matter so much that he didn’t wipe his feet, now."
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done
                                                    "Step towards him ":
                                                        m "That’s right, this way."
                                                        m "But not over there"
                                                        m "those are where I keep the Stradyl samples."
                                                        m "They are poisonous mushrooms, causing whoever eats them to reveal their darkest, innermost and most likely embarrassing secret before dying from explosive diarrhea."
                                                        m "But you don’t care about those, do you?"
                                                        menu:
                                                            "Eat the mushrooms":
                                                                e "Using reverse psychology, eh? Ha, I’ll eat them all at once!"
                                                                "*Bryant Runs over and eats a few at once*"
                                                                e "I THINK MY MOM IS HOT, AND I STILL PISS MY BED SOMETIMES!"
                                                                e "WAIT, WHAT THE HECK, OH MY GOD, I HAVE TO TAKE A DUMP REAL BAD! AGHHHHH!"
                                                                e "“SHIT, SHIT, SHIT!!! LITERALLY, SHIIIITTTT! AAAAAHHH!!!"
                                                                e "BY THE WAY, I REALLY LIKE BOY BANDS AND I THINK MOST OF THE SINGERS ARE KINDA CUTE BUT I’M NOT GAY… I THINK…"
                                                                e "AAHHHHHHHHHHH!!!"
                                                                m "-...I should have thought that one through."
                                                                scene bg death
                                                                stop music
                                                                play music "scary_music.ogg"
                                                                pause
                                                                jump choice0_done
                                                            "Keep walking":
                                                                e "Um, err, no thanks"
                                                                m "On a one track mind today, aren’t we, mortal?"
                                                                m "I suppose I can’t distract you with that pile of currency next to the collection fairly lethal shock rune?"
                                                                menu:
                                                                    "Go get the money":
                                                                        e "Well, free money can’t be that bad, I suppose."
                                                                        e "Wow, this is actually a lot-"
                                                                        e "OWOWOWOW HOW UNEXPECTED OWOWOW!"
                                                                        scene bg death
                                                                        pause
                                                                        jump choice0_done
                                                                    "Keep walking":
                                                                        e "Hey, quit pointing out all the lethal things in the room as I walk towards you."
                                                                        m "But then how else would you know about the trapdoor that leads to a pit of man eating parakeets underneath that rug there?"
                                                                        menu:
                                                                            "Check under the rug":
                                                                                e "Man eating parakeets? Yeah right, probably man tickling at worst"
                                                                                hide bryant
                                                                                e "C’mon out, little birdies. Actually, I’ve always wanted a pet-"
                                                                                e "OW! That hurts, knock it off! HEY, NO! NO! AAARRRGGGHHH!"
                                                                                e "*burp*"
                                                                                m "(...I knew there was a reason to keep those things around.)"
                                                                                scene bg death
                                                                                stop music
                                                                                play music "scary_music.ogg"
                                                                                pause
                                                                                jump choice0_done
                                                                            "Keep walking":
                                                                                e "Enough! I’m obviously just going to keep walking, now just hold tight"
                                                                                m "Keep walking, eh? Even if I conjure a rebounding force field in front of me?"
                                                                                show forcefield normal at right
                                                                                menu:
                                                                                    "Go around it ":
                                                                                        e "So I’ll just walk around it, I have common sense."
                                                                                        hide forcefield normal
                                                                                        m "Do you?"
                                                                                        m "Or do you realize now that maybe someone else does too?"
                                                                                        m "Maybe it’s something different than common sense"
                                                                                        m "sympathy."
                                                                                        m "Someone who doesn’t know you personally, who wouldn’t lose anything from your death or injury, decided to help you pass the challenges and avoid a thousand terrible fates."
                                                                                        m "He helped you discover the clues, pass the challenges, uncover secrets, and defeat remarkable wizards."
                                                                                        m "For what?"
                                                                                        m "Do you think he gets something for breaking the curse?"
                                                                                        m "Some prize or reward"
                                                                                        m "a medal of honor?"
                                                                                        m "Was it for his own amusement?"
                                                                                        m "Is he just that bored?"
                                                                                        m "Or perhaps some people prefer Naches, rather than Schadenfreude?"
                                                                                        m "Yes, someone put their thoughts and feeling through your eyes."
                                                                                        m "They imagined what they would have felt for you, even though you’re nothing more than a doll to them."
                                                                                        m "Empathy and sympathy, one of the greatest advancements humanity can ever achieve"
                                                                                        m "those things brought you here, before me."
                                                                                        m "I think you’ve learned something too" 
                                                                                        m "perhaps unconsciously, perhaps forced, perhaps innate in your very being."
                                                                                        m "Trust."
                                                                                        m "You trusted your puppeteer to do the right thing."
                                                                                        m "You knew he could."
                                                                                        m "And he didn’t let you down, with nothing going for him but your hopes and dreams on the line."
                                                                                        m "This is what the curse is meant to teach, and this is what I believe you have finally learned."
                                                                                        m "I humbly offer you my hat, and with it, your life."
                                                                                        menu:
                                                                                            "Ask about the blatant plot holes":
                                                                                                e "..."
                                                                                                m "..."
                                                                                                e "What the heck is that load of crap?"
                                                                                                m "Eh?"
                                                                                                e "All your friends, except the red one maybe, seemed to not give a shit if I learned anything or not."
                                                                                                e "Actually, the yellow one flat out tried to kill me."
                                                                                                e "Uh…well…"
                                                                                                e "And how can you act like this was all some stupid learning experience?"
                                                                                                e "It was going to kill me after %(difficulty)d days, and you probably wouldn’t even remember if it wasn’t for me coming over here to remind you, right?"
                                                                                                e "And this whole thing started when he made me do all that weird stuff on the first day, right?"
                                                                                                e "How is that trust building?"
                                                                                                m "NO…um…uh…"
                                                                                                e "What’s the point of making me learn, anyways?"
                                                                                                e "Do YOU get a medal or something, huh? What?"
                                                                                                m "Well, I mean, it’s more…uh…"
                                                                                                e "Not that you probably thought that far ahead, right?"
                                                                                                e "All those lethal traps you were pointing out was probably just you hoping whoever was controlling me would ram me into them, right?"
                                                                                                m "Hey…there’s no, proof…umm…"
                                                                                                e "How are you casting all these spells, anyway?"
                                                                                                e "How has no one found out about all this voodoo magic when you’re screaming your heads off about dolls and casting force fields all over the place?"
                                                                                                m "Actually, there’s a very logical explanation-"
                                                                                                e "That involves more “deus ex machine” magic, right?"
                                                                                                e "What the heck do half your spells have to do with Puppeteering, anyways?"
                                                                                                e "Unless puppets have something to do with force fields that I’m currently unaware of."
                                                                                                e "How did you learn that crap anyways?"
                                                                                                e "Is there some science behind it?"
                                                                                                e "How do you just arbitrarily give control of my actions to some unknown force possibly a thousand miles away just by chanting?"
                                                                                                e "What’s up with your friends anyways?"
                                                                                                e "Is magic inversely proportional to common sense or something?"
                                                                                                e "You apparently have infinite magical powers but you go about your day cursing retailers and stealing burgers?!"
                                                                                                e "Also, did you curse all the cops in the city or something?"
                                                                                                e "They each have their own personal emotional problems that apparently hinder their cognitive skills."
                                                                                                e "Most serious crimes are only worth half a day in jail, where they conveniently release me with just enough time to go home."
                                                                                                e "What if the unknown force had “save files” or something?"
                                                                                                e "Couldn’t they just be throwing me into every possible danger for their own sadistic amusement then reloading till they got the ending right with sheer luck?"
                                                                                                m "Now you’re just making things up-"
                                                                                                e "THIS WHOLE FUKING PLOT IS MADE UP, AHH!!!"
                                                                                                m "Chill, mortal."
                                                                                                e "Why do you call everyone mortal?"
                                                                                                e "Are the magicians immortal or something?"
                                                                                                e "Puppeteers I mean?"
                                                                                                e "Why do you call yourselves puppeteers if I never see anything puppet related come out from you-"
                                                                                                m "FINE, GEEZ, NOTHING MAKES SENSE, OK? YOU WIN!"
                                                                                                m "Now just take my hat and be happy the curse is gone."
                                                                                                hide magicianred
                                                                                                show magician normal at right
                                                                                                e "How does just having the hats break the curse?"
                                                                                                e "Didn’t you chant something to curse me?"
                                                                                                e "Shouldn’t there be a “counter-curse” or something more complicated than just having your 4 hats with me?"
                                                                                                e "And what’s with your hats?"
                                                                                                e "Do you lose your power when they’re gone or something?"
                                                                                                e "Why else would it be important to collect them if-"
                                                                                                m "Urg, forget this. I’m out."
                                                                                                e "OUT?!?!"
                                                                                                e "HOW?!?"
                                                                                                e "DOES TELEPORTING NOT NEED TO BE CHANTED OR SOMETHING?"
                                                                                                e "CAN’T YOU CURE WORLD HUNGER OR SOMETHING WITH ALL THAT POWER?"
                                                                                                m "Magic, bitch, I don’t have to explain shit. Peace out."
                                                                                                play sound "spell.ogg"
                                                                                                hide magician
                                                                                                e "NOOOOO"
                                                                                                e "How am I going to live with all these obvious inconsistencies in my world, now?"
                                                                                                e "Am I just going to ignore the fact there’s some crazy magic bastard with no common sense just wandering around?"
                                                                                                e "And what am I going to do with all this lethal stuff he just left behind?"
                                                                                                e "..."
                                                                                                e "Oh, that’s right, those options aren’t coming up anymore."
                                                                                                e "I’m free!!!"
                                                                                                jump cryptlast2
                                                                                            "Punch him in his stupid, psychotic little weirdo face ":
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OW! What the hell, mortal?"
                                                                                                e "What the hell?"
                                                                                                e "WHAT THE HELL?"
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OWWW!"
                                                                                                e "You, and your weirdo friends."
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OWWW, STOP IT"
                                                                                                e "Dump some lethal brainwashing crap on me…"
                                                                                                e "You make me run around town for days solving your stupid shitty puzzles…"
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OWCH, KNOCK IT OFF!"
                                                                                                e "You tried to kill me off multiple times, and to tell me I fucking deserve it…"
                                                                                                play sound "punch.ogg"
                                                                                                show bryant punch at center
                                                                                                pause
                                                                                                show bryant normal at left
                                                                                                m "OOWWWW!!!"
                                                                                                e "AND YOU THINK I’M JUST GONNA DROP ALL THAT IF YOU TELL ME SOME SOB STORY ABOUT LEARNING TO TRUST THE FUCKING PSYCOPATH WHOSE BEEN MAKING ME DO ALL THIS WEIRD SHIT IN THE FIRST PLACE?!?!?”"
                                                                                                e "OW, FORCE FIELD, OW!"
                                                                                                show forcefield normal at right 
                                                                                                e "WHOA!"
                                                                                                m "FINE, WHATEVER, GEEZ, JUST TAKE THE HAT!"
                                                                                                m "I DON’T GIVE A CRAP IF YOU LEARNED ANYTHING NOW!"
                                                                                                hide magicianred
                                                                                                show magician normal at right
                                                                                                m "BIBBIDY BOBBIDY BOO!"
                                                                                                m "CURSE UNDO AND STUFF!"
                                                                                                m "Good day!"
                                                                                                m "TELEPORTING OUT!"
                                                                                                m "CRAAAP"
                                                                                                play sound "spell.ogg"
                                                                                                hide magician
                                                                                                e "Well shit, what am I going to do with all these hats, now?"
                                                                                                e "Wait, that’s right, I’m free!"
                                                                                                jump cryptlast2
                                                                                            "Just roll with it for the corny ending, already ":
                                                                                                e "..."
                                                                                                e "You’re right, you are completely right."
                                                                                                e "All this time, he’s actually been helping me along."
                                                                                                e "I guess I just unconsciously just felt normal, you know?"
                                                                                                e "He knew what I had to do, and helped me achieve my goal."
                                                                                                e "Even back at that nightclub, he helped me dodge bullets, I mean-"
                                                                                                m "The puppet often feels like it can do more than it ever could, when the puppeteer brings it down from the shelf."
                                                                                                m "And with your experiences in tow, you now have the chance to be the puppeteer of your own life."
                                                                                                hide magicianred
                                                                                                show magician normal at right
                                                                                                m "With the hats in your possession the curse is undone entirely."
                                                                                                m "Your actions are now forever your own."
                                                                                                m "You can go back to your “average life” back in that bookstore…"
                                                                                                m "But after that amazing performance,"
                                                                                                m "Who could be content with such a repetitive act, eh?"
                                                                                                m "my brethren and I will bother you no more."
                                                                                                m "We were planning to go back to Florida soon."
                                                                                                m "There are a lot more people like us there"
                                                                                                e "You mean complete weirdoes or magicians?"
                                                                                                m "Only weirdoes, but we could use the company sometimes."
                                                                                                m "Farewell, Bryant Day."
                                                                                                hide magician 
                                                                                                play sound "spell.ogg"
                                                                                                e "Whoa, he teleported out."
                                                                                                e "…Well, now what should I do?"
                                                                                                e " ... "
                                                                                                e "…Oh, wait, that’s right."
                                                                                                e " I'm free!"
                                                                                                jump cryptlast2
                                                                                                
                                                                                                label cryptlast2:
                                                                                                        stop music
                                                                                                        play music "main.ogg"
                                                                                                        scene bg graveyardnight
                                                                                                        show bryant normal at center
                                                                                                        e "Well, now that that’s all over with, life can finally return to normal."
                                                                                                        scene bg burgerstore
                                                                                                        show bryant normal at left
                                                                                                        e "But how have things changed?"
                                                                                                        e "Hmmm…"
                                                                                                        e "Well I’m still alive, aren’t I?"
                                                                                                        e "And I guess I still have my job to return to ..."
                                                                                                        scene bg citysidewalk
                                                                                                        show bryant normal at left
                                                                                                        if (hobo < 2):
                                                                                                            show hobo normal at right
                                                                                                            e "Hmmm, I don’t think I’m in trouble with the law anymore…"
                                                                                                            h "Hey, gimmie some cash, kid."
                                                                                                            e "Not in the mood, hobo."
                                                                                                            h "Piss off then, you arrogant little terd! *mumble mumble*"
                                                                                                        else:
                                                                                                            e "Hmmm, I don’t think I’m in trouble with the law anymore…"
                                                                                                            e "..."
                                                                                                            if(hobo == 2):
                                                                                                                e "Oh that’s right... The hobo left..."
                                                                                                                e "Another thing to look forward to."
                                                                                                            else:
                                                                                                                e "Oh that's right... I assassinated lord hobo..."
                                                                                                                e "Still don't know how I feel about that..."
                                                                                                        scene bg alley
                                                                                                        show bryant normal at right
                                                                                                        if (bank == 0):
                                                                                                            e "Oh, that’s right!"
                                                                                                            e "I spent all my saving didn’t I…"
                                                                                                            e "..."
                                                                                                            e "Okay, so that’s a problem…"
                                                                                                        else:
                                                                                                            "I’ve still got some money saved up in the bank, I can pay off any debts I owe…"
                                                                                                        scene bg apartmentday
                                                                                                        show bryant normal at center
                                                                                                        e "Overall, I guess things turned out pretty ok."
                                                                                                        e "I can go back to work tomorrow, and no one will ever realize what happened."
                                                                                                        e "I can be perfectly average again."
                                                                                                        e " Well, maybe it WOULD get a little boring being average ALL the time…"
                                                                                                        e "… And that puppeteer…"
                                                                                                        e "I guess he wasn’t really such a bad dude, after all."
                                                                                                        if (evedate == 1):
                                                                                                            e "Oh wait, there’s a message on my phone from eve."
                                                                                                            e "Oh wait, that’s right!"
                                                                                                            e "We’re dating now!!!"
                                                                                                            e "..."
                                                                                                            e "You really weren’t a bad guy at all, were you, my puppeteer wingman?"
                                                                                                        if (evedate == 1) and (hobo == 3) and (assasin == 1):
                                                                                                            e "Wait, another message?"
                                                                                                            e "…and who is this from?"
                                                                                                            e "…Al Capone?"
                                                                                                            e "…oh, right, the hobo is gone, so…"
                                                                                                            e "... I guess I’m an assassin as well…"
                                                                                                        elif (hobo == 3) and (assassin == 1):
                                                                                                            e "…wait, what’s this message on my phone?"
                                                                                                            e "…It’s from…"
                                                                                                            e "…Al Capone?"
                                                                                                            e "…oh, right, the hobo is gone, so…"
                                                                                                            e "... I guess I’m an assassin as well…"
                                                                                                        scene bg title with fade
                                                                                                        pause
                                                                                                        scene bg credit with fade
                                                                                                        pause
                                                                                                        scene bg credit2 with fade
                                                                                                        pause
                                                                                                        jump choice0_done
                                                                                                   
                                                                                        
                                                                                        
                                                                                    "Keep walking":
                                                                                        e "Well, I can’t just stop halfway, right? That’d be like giving u-"
                                                                                        e "WOAAA!!!"
                                                                                        m "(Oh, snapped his neck.)"
                                                                                        m "(…Perhaps I should have mentioned how strong the rebounding effect was…)"
                                                                                        m "(…Eh, he should have guessed it himself by now.)"
                                                                                        scene bg death
                                                                                        stop music
                                                                                        play music "scary_music.ogg"
                                                                                        pause
                                                                                        jump choice0_done
                                    else:
                                        e "It’s the cemetery"
                                        e "no one I know is dead yet, so there’s no real-"
                                        e "*AUUGG*…What’s that sound?"
                                        play sound "spell.ogg"
                                        e "Urgh…it’s making…me…ugh…"
                                        e "This…is bad..."
                                        label cemetarychoice2:
                                            menu:
                                                "Head towards the noise":
                                                    jump choice26_cryptb2
                                                "Sing louder than the noise":
                                                    jump choice26_loudb2
                                                "Tell the noise to shut up ":
                                                    jump choice26_shutupb2
                                                "Run away":
                                                    jump choice26_runb2
                                        label choice26_cryptb2:
                                                e "(Gah…if I reach the noise…then…maybe…)"
                                                e "(Urg…)"
                                                e "...."
                                                e "Ah…blacking…out…"
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                        label choice26_loudb2:
                                                e "MARY HAD A LITTLE… Urgh…"
                                                e "ALL THE SINGLE LADIES…all…the…"
                                                e "Urgh…IT’S THE…EYE OF THE… tiger…"
                                                e "WALK UP…in…the club…like…what up…I got…a…big…err…"
                                                scene bg citysidewalk
                                                show citizen normal at right
                                                c "(What’s with that weird music at the cemetery? It’s been playing like that for a few days.)"
                                                c "(Oh, there goes someone to check. Maybe he’ll make them turn it off)"
                                                c "(Eh? Is he sick or something? He doesn’t look to goo-)"
                                                e "MARY HAD A LITTLE… Urgh…"
                                                e "ALL THE SINGLE LADIES…all…the…"
                                                e "Urgh…IT’S THE…EYE OF THE… tiger…"
                                                e "WALK UP…in…the club…like…what up…I got…a…big…err…"
                                                c "And he collapsed…"
                                                c "I think I’ll just keep walking"
                                                scene bg death
                                                pause
                                                jump choice0_done
                                        label choice26_shutupb2:
                                                e "GODDAMMIT, SHUT UP."
                                                "*Music continues to play*"
                                                e "Ugh…"
                                                jump cemetarychoice2
                                        label choice26_runb2:
                                            e "Urg…got to, get away…"
                                            scene black
                                            "*Hours later*"
                                            scene bg graveyardnight
                                            show bryant normal at left
                                            e "Urg…"
                                            e "Ugh, that music is still going on-"
                                            e "Wait, its night already?!? I must have been passed out for most of the day!"
                                            e "I shouldn’t even bother trying to walk back into it, it’d be suicide for sure."
                                            e "There’s nothing else I can do now"
                                            e "I might as well head back home."
                                            jump apartmentn2
                                                
                                    jump map2
                                elif result == "sidewalk":
                                    scene bg citysidewalk
                                    show bryant normal at left
                                    if (hobo >= 2):
                                        e "(It’s the sidewalk on my way to work, but beggar free.)"
                                        if(hobo == 3):
                                            e "(I don't know how I feel about having killed him...)"
                                        else:
                                            e "(It was worth the $200.)"
                                        e "(When this curse is all sorted out, I’ll be able to walk to work without someone screaming obscenities at me and demanding small change.)"
                                        e "(Maybe I’ll miss him; he seemed to liven up a bit when I gave him a little.)"
                                        e "..."
                                        e "Nawww..."
                                        jump map2
                                    show hobo normal at right    
                                    e "(Nothing special here, though it is on my path to work.)"
                                    e "(Oh, wait, right.)"
                                    e "(The hobo...)"
                                    if (hobo == 0):
                                        h "Ay, you! Yeah, you! Gimmy some cash, you’re just gonna waste it anyway."
                                    else:
                                        h "Oh, its you again. Spare anything else fer a starving beggar?"
                                    label swalkchoice2:
                                        menu:
                                            "Ignore him and leave":
                                                h "Yeah, keep walkin sonny. I’ll stay right here, waiting for someone to give a crap."
                                                jump map2
                                            "Ask about him ":
                                                jump choice22_ask2
                                            "Give him 100$ ":
                                                jump choice22_give2
                                            "Punch him":
                                                jump choice22_punch2
                                            "Help him get a job ":
                                                jump choice22_job2
                                        label choice22_ask2:
                                            if (hobo == 0):
                                                e "How’d you end up here anyway? And don’t you ever go anywhere else? To eat or something?"
                                                h "Oh, look at sonny boy here, eh, pretending to care but won’t cough up any cash. What a faker, spoiled bourgeoisie 92 percent something or other grumble grumble."
                                                e "People might jump for a sob story? "
                                                e "Can you make anything up at least?"
                                                h "You calling me a sob? I’ll sob you, you... Damn kids mocking me when I’m down on my luck."
                                                e "Come on, anything about yourself?"
                                                h "I need cash, asshole. Gimmy whatever you got."
                                                jump swalkchoice2
                                            else:
                                                e "Whats your story?"
                                                h "Me? Eh, I was always like this. Really. Can’t remember much else."
                                                e "What, you were born begging?"
                                                h "Well, I mean, uhhh... Well, I guess I did... live in... ehh... ummm..."
                                                h "Kinda a large family... erm... eh... not much to... ah... eat..."
                                                h "Oh darn it, I lived in a mansion."
                                                e "Woa, unexpected. What happened?"
                                                h "Uh... ah... ehhh..."
                                                e "What, were your parents overly flamboyant and arrogant about rich, giving you a complex against those with high social status and causing you to alienate yourself from them in an act of defiance and run away to become a homeless vagabond?"
                                                h "What? Fuck no, I gambled till they threw me out."
                                                e "HA! Knew it."
                                                h "Shut up, you lucky little sob... grumble grumble..."
                                                jump swalkchoice2
                                        label choice22_give2:
                                            e "Here, have some cash."
                                            if (money == 0):
                                                e "... Uh, actually, it seems I don’t have any money on me."
                                                h "Oh, riiight, I get that all the time, asshole. All you snobs and your fancy coats and your fancy hats with your “Oh, I don’t have any spare money for a starving man”."
                                                h "Well then why don’t I see you sitting down here with me? Huh?"
                                                e "Because we go out to work for money?"
                                                h "... Fuck you."
                                                jump swalkchoice2
                                            elif (hobo == 0):
                                                $ money -= 100
                                                $ hobo += 1
                                                h "Now we’re talkin, sonny. This much will keep me steady for weeks."
                                                jump swalkchoice2
                                            else:
                                                $ money -= 100
                                                $ hobo = 2
                                                h "Well holy crap. Aren’t you the bees knees."
                                                h "With this much moolah, I don’t need to sit here rotting up the place anymore."
                                                h "I’ve got enough to live out my dreams now. Thanks a lot kid, you’ve given me a brand new faith about this whole “humanity” thing!"
                                                e "You know, it's entirely possible for you to work for that money yourself."
                                                h "Don’t push your luck, kid."
                                                h "I’m off for adventure. Good luck with whatever shit you’re doing, I guess."
                                                show hobo happy at offscreenright with move
                                                e "(Well, at least in the end, he finally learned to say thank you.)"
                                                e "(In a way, I guess.)"
                                                e "(And, actually, it did kinda cost 200$ overall...)"
                                                e "..."
                                                e "(Hobo's gone. Worth it.)"
                                                e "(Now, back to the curse...)"
                                                jump map2
                                        label choice22_punch2:
                                            e "Want some food instead?"
                                            h "Eh?"
                                            e "How’s about a knuckle sandwich?"
                                            show policeman normal at offscreenright
                                            show policeman normal at center with move
                                            p "Hold it right there, bub."
                                            e "Wait, what?!? Where did you come from?"
                                            p "I’ve been here the whole time. The city’s got a special division posted just for defending this hobo."
                                            h "Oh, shit! Get him, officer! Blow his frickin' brains out!"
                                            e "You’re telling me the city has an entire police division just for defending this annoying prick?"
                                            h "Officer! He’s crazy, I tell ya! Went feral right in front of me, he did!"
                                            p "Think about it: in every successful city, you always think of hobos panhandling on the street, right?"
                                            p "This guy here’s the last homeless man in the city."
                                            p "If we lose him, it's like we’re losing part of the qualification."
                                            h "You tell him, officer! Beat the crap outta him!"
                                            e "So you have an entire division defending him just because his social status makes your workplace more diverse? I should sue for discrimination!"
                                            p "Doesn’t matter why we’re defending him, bub; I caught you red handed about to lay hands on this beggar."
                                            h "Hey, officer? Can I get his wallet?"
                                            e "So what’s the punishment then?"
                                            p "You’ll be-"
                                            h "Hey officer! His walle-"
                                            p "FOR FUCK'S SAKE, SHUT UP."
                                            h "..."
                                            p "..."
                                            p "Jesus, I gotta hear you beg all day, but I ain’t tolerating this shit."
                                            e "...so my punishment?"
                                            p "... Well, I guess I can’t really blame you for wanting to beat the shit outta him... How’s about I just hold you at the station for a while and let you go at sunset?"
                                            e "Fine with me."
                                            h "... Pig cops, conspiring against me with rich snobs, grumble grumble."
                                            scene black
                                            "*hours later*"
                                            jump apartmentn2
                                        label choice22_job2:
                                            e "Why don’t you get a job?"
                                            h "They think they’re too good for me... Well I’m too good for them. They just don’t know it, I’ll have you know."
                                            e "Why don’t you let them know instead?"
                                            e "Look, I can see a help-wanted poster across the street. Just ask for some work there."
                                            h "Da-fucks your problem, boy? Don’t butt in on other people’s business. Look at you, mocking a poor beggar."
                                            e "But you were just asking me for money a second ago."
                                            h "Now what, you’re bragging about it?"
                                            h "Probably some rich snot with nothing better to do than annoy me, rather than helping me with some cash, eh, aren’t you? Feels good, rich boy? Having fun?"
                                            e "(Ugh... This isn’t working at all.)"
                                            jump swalkchoice2
                                        

                                               
                                                
                                                
                                                
                                                
                                                
                                            
                                            
                                            
                                            
                                            
                                    
                                    
                                        
                                    jump map2
                                elif result == "statue":
                                    if (statuedestroyed == 2):
                                        jump statue62
                                    elif (statuedestroyed == 3):
                                        jump statue92
                                    elif (statuedestroyed == 1):
                                        scene bg citystatue
                                        show bryant normal at left
                                        e "Here’s the town statue, made in the image of our apparently very vain mayor."
                                    else:
                                        scene bg citystatue
                                        show bryant normal at left
                                        e "Here’s the town statue, made in remembrance of some famous dead guy I don’t know."
                                        e "Nothing to do here."
                                        e "There’s not even anyone around."
                                        label statuechoice2:
                                        menu:
                                            "Leave":
                                                e "Right then, back to questing."
                                                jump map2
                                            "Read about the statue":
                                                jump choice13_read2
                                            "Vandalize the statue":
                                                jump choice13_vandalize2
                                        label choice13_read2:
                                            #$ statuedestroyed == 1
                                            e "Let's see, says here..."
                                            e "... Famous dead guy... is actually the mayor. Guess he’s still living, actually..."
                                            e "Wait, that means I had no idea what the mayor looked like until now."
                                            e "Well then, I guess that means it didn’t matter until now."
                                            e "Learn something new every day when mystical unknown forces control your every move, I suppose."
                                            jump statuechoice2
                                        label choice13_vandalize2:
                                            e "Vandalize public property, why not."
                                            $ statuedestroyed = 2
                                            scene black
                                            "*Hours later*"
                                            scene bg citystatuedestroyed
                                            show bryant normal at left
                                            e "After hours of hard work and dedication, I’ve reduced a monument in someone’s honor to a ugly looking scrap heap. I don’t think I’m liking this curse at all..."
                                            show policeman angry at offscreenright with move
                                            show policeman angry at right with move
                                            p "Hold it right there, scumbag."
                                            e "Oh, shit! It's the fuzz!"
                                            e "Actually I’ve been vandalizing a public statue in the middle of a street for a few hours now. Why am I surprised the police showed up?"
                                            e "Actually, its kinda strange it took them so long to notice. It took me a good hour or two to rip off the head, and I was on top of it prying the whole time."
                                            p "That’s enough of your derogatory monologue. You’re under arrest for vandalism, buddy!"
                                            menu:
                                                "Give up":
                                                    e "I give up, take me away."
                                                    p "Not gonna try and run away? Good."
                                                    label statuevchoice2:
                                                        p "Normally vandalism of this scale would get you sent away for a year or two, but the mayor said it was his statue, and he doesn’t mind."
                                                        e "Oh, wow. This mayor sounds like a real nice guy."
                                                        e "Makes me kinda feel bad for vandalizing a statue of him for the past couple hours."
                                                        p "Yeah, well feel bad about it for a few hours more. We’re still locking you up for the rest of the day, so don’t get too smug."
                                                        e  "Don’t worry, I won’t."
                                                        scene black
                                                        "*Hours later*"
                                                        jump apartmentn2
                                                "Run for it ":
                                                    e "Uh, look over there, a dog with a curly tail!"
                                                    p "Oh? Where? You mean behind the massive vandalized statue?"
                                                    show bryant normal at left with move
                                                    show bryant normal at offscreenleft with move
                                                    p "I don’t see- ohhh, I get it."
                                                    p "There wasn’t any dog at all. I was fooled."
                                                    p "Clever move, mystery vandal, very clever indeed."
                                                    jump map2
                                                "Duke it out with him ":
                                                    e "Hows about I smack you one in the gob and make off into the sunset scot free instead, “buddy”, eh? Whatdayathink of that?"
                                                    p "I think I have a gun."
                                                    e "Oh."
                                                    e "Right..."
                                                    e "I keep forgetting these simple thi-"
                                                    show policeman shooting at right
                                                    pause
                                                    scene bg death
                                                    stop music
                                                    play music "scary_music.ogg"
                                                    pause
                                                    jump choice0_done
                                    label statue62:
                                        scene bg citystatuedestroyed
                                        show bryant normal at left
                                        e "Here’s the town statue. That I vandalized. Hm."
                                        e "Nothing to do here."
                                        e "There’s not even-"
                                        e "Loljk there’s a cop right behind me..."
                                        show policeman normal at right
                                        p "Excuse me sir, do you happen to know anything about what occurred here?"
                                        p "Actually, you look kinda familiar ..."
                                        menu:
                                            "Admit it":
                                                e "Oh, yeah, um, this was kinda my fault."
                                                p "I knew it! The perpetrator always returns to the scene of the crime!"
                                                p "And there are no dogs with curly tails in a 10 mile radius, I checked, so you can’t fool your way out of this one!"
                                                jump statuevchoice2
                                            "Deny it ":
                                                e "Uh, no, no idea, what, does this place not normally look like this?"
                                                p " ..."
                                                p "Eh, no, it doesn’t. We’re still looking for the vandal who did it."
                                                p "He looks exactly like you, though. So if you see anyone who looks exactly like you in every way, bring him in for questioning please."
                                                e "Uh, sure thing officer."
                                                e "What is with all the cops around here? If I knew they were this stupid before this whole curse thing, I’d forget the whole average business and just go around robbing banks in broad daylight."
                                                e "Doesn’t matter, I guess. At least I’m off the hook for now."
                                                jump map2
                                            "Punch him in the face":
                                                p "Does THIS look familiar?"
                                                p "Oh no! He’s armed with an arm! And he’s running straight for my face from 10 feet away!"
                                                p "Good thing I’m a cop with a gun and the right to defend myself."
                                                show policeman shooting at right
                                                e "Oh, right, that."
                                                scene bg death
                                                stop music
                                                play music "scary_music.ogg"
                                                pause
                                                jump choice0_done
                                    label statue92:
                                        e "There’s the statue I vandalized..."
                                        e "Hm, its been a day or two but they still haven’t picked up the place at all."
                                        e "Was I suppose to clean it up for community service or something? All they did was lock me in a cell for most of the day and told me I was free to go back home..."
                                        e "Maybe they’re leaving it for other criminals to clean up for THEIR sentences or something?"
                                        e "Or maybe they like what I did with it. It kinda looks like modern art, sorta."
                                        e "Not very average, like it was before, but for statues average means ugly and ignorable, so its kind of an improvement."
                                        e "The graffiti was actually a nice touch. They really should have paid me instead of arresting me."
                                        e "..."
                                        e "Now that I think about it, I can’t believe I just said that."
                                        e "I am turning more and more unaverage by the day, aren’t I?"
                                        e "Ugh, gotta hurry up and find a cure for this curse."
                                        jump map2
                                                
                                                
                                    jump map2
                                elif result == "nightclub":
                                            scene bg nightclub
                                            show bryant normal at offscreenleft
                                            show gangster normal at center
                                            show gangster2 normal at right
                                            show bryant normal at left with move
                                            
                                            #if (nightclubdone):
                                            #    "Nothing to do here."
                                            #    jump map2
                                            
                                            e "Oh geez, this has to be the shadiest place I’ve ever unwillingly visited in my entire average life."
                                            g "Hey, what do you want?"
                                            
                                            label nightclubmenu12:
                                                menu:
                                                    "Leave":
                                                        e "Uh, umm, I’ll just be leaving..."
                                                        g "Right on, brutha. Peace, dawg."
                                                        jump map2
                                                    "Ask for drugs":
                                                        jump nightclub_22
                                                    "Repremand them":
                                                        jump nightclub_32
                                                    "Ask to talk to their boss":
                                                        jump nightclub_42
                                                    "Pretend to be a cop":
                                                        jump nightclub_62
                                                    
                                            label nightclub_22:
                                                e "Hey, uh, you got any drugs?"
                                                g "Woa, dog, drugs ain’t cool."

                                                g2 "Yeah man, Don’t they burn your brain and stuff? Unhealthy shit, man."

                                                e "Oh, right. Sorry for asking."

                                                g "Treatin us like a coupla dealers, fool. No respect."
                                                jump nightclubmenu12
                                                
                                            label nightclub_32:
                                                e "Look at yourselves. Can’t you think of anything better to do than play “gangster” and cause suffering for your own selfish gain?"

                                                g "Whoa, dog, don’t you be judging us."

                                                g2 "Yeah, man, I gotta get some money for my momma’s operation, or she’s wasted bro!"

                                                g "And my sister, dude, she’s coughin' and weezin' up a storm back home."
                                                g2 "You sayin' that we should sit tight while our family’s at death's door bro?! You sayin' you wouldn’t man up and do whatever you needed to do for yo family? Huh?!"

                                                e "Oh, geez, I didn’t know...Sorry."

                                                g2 "Ha, we're just messin with you fool.It's all for the cash."

                                                g "Yeah, all for the cash, brutha. Rakin' in the dough, make it rain, holla at ya boy, ya know?"

                                                e "…"

                                                g2 "Ha, spud don’t know. Little pussy if I ever saw one, and I saw plenty, let me tell ya."

                                                g "Haha, you tell him, man."
                                                jump nightclubmenu12
                                                                            
                                            label nightclub_42:
                                                e "I want to talk to your boss."

                                                if(hat < 2):
                                                    g2 "The boss? He don’t want to waste his time on creeps like you."

                                                    e "What, is he scared of me before he meets me? Coward ain’t worth my time, then."
                                                    show boss normal at offscreenright
                                                    show boss normal at right with move

                                                    mb "Not worth your time, am I?"

                                                    e "Oh, shit!"

                                                    g "Boss! We don’t know this guy, he just came in askin' for you."

                                                    mb "I can see that. He must be here for something very important to have the balls to insult me on my own territory. Well, kid, what do ya want?"

                                                    e "Oh, er, um I-"
                                                    menu:
                                                        "Leave":
                                                            e "I’ll just be leaving, then?"
                                                            
                                                            show boss happy
                                                            mb "You think you can insult the next great Capone and get away with it? Waste him, boys."
                                                            play music "gunshot.wav"
                                                            show gangster animated
                                                            show gangster2 animated
                                                            e "Aw, shiiiiiiiii-"
                                                            pause
                                                            stop music 
                                                            play music "scary_music.ogg"
                                                            scene bg death
                                                            pause
                                                            jump choice0_done
                                                        "Ask to be his personal assassin":
                                                            jump nightclub_4_22
                                                        "Punch him":
                                                            jump nightclub_4_32
                                                        "Compliment him":
                                                            jump nightclub_4_42
                                                        "Tell him you're an undercover cop":
                                                            jump nightclub_4_52
                                                                      
                                                elif(hat > 2):
                                                    g "Sorry, bro. That voodoo priest dude high tailed it outta here after you pulled off those mad jukes, bro."
                                                    g2 "Old Capone came back, but he ain’t feelin' so hot after the full fiasco, you know what I’m sayin'?"

                                                    e "Yeah, anyone would be sick after dealing with those wizards."

                                                    g "You got it, bro."
                                                    jump nightclubmenu12
                                                else:
                                                    jump nightclub_52


                                                label nightclub_4_22:
                                                        $ assassin = 1
                                                        e "I’ve come to be your personal assassin."
                                                        
                                                        if(hobo == 3):
                                                            mb "What do you mean? You already killed the hobo. If this is all you wanted, I'm out of here."
                                                            show boss normal at offscreenright with move
                                                            jump nightclubmenu12

                                                        mb "Eh? You want to be my hit man?"
                                                        mb "Well, you do look pretty average… No one would suspect a guy like you to be a stone cold killer."

                                                        e "Yeah, hehe, uh…"
                                                        
                                                        if(hobo == 2):
                                                            mb "I would ask you to assassinate the hobo as a test, but I haven't seen him around lately..."
                                                            mb "What else do you want?"
                                                            show boss normal at offscreenright with move

                                                            e "Oh, hey, I’m alive. How bout that."

                                                            g2 "You got lucky, kid; not many get away so lightly with insultin the boss."

                                                            e "Won’t happen again."

                                                            g "Damn right."
                                                        
                                                            jump nightclubmenu12
                                                            

                                                        mb "Tell ya what: if you prove yourself with an easy hit, I’ll forgive your sorry ass. Whack that annoying ass hobo I keep seein' on the streets."

                                                        e "Eh? You mean that ungrateful sob who treats you like scum if you don’t fork over everything you've got?"

                                                        mb "Yeah, that’s the one. Make it clean, too; get him gone, and don’t leave a trace. Could've just walked outta town, the cops wouldn’t know any better."

                                                        e "Right, discreetly kill the hobo and I’ll earn your trust."
                                                        e "I never thought I’d ever be saying that, but here I am."

                                                        mb "Hehe, you got some spunk kid. Now go show me some discretion."
                                                        menu:
                                                            "Assassinate Lord Hobo":
                                                                $ hobo = 3
                                                                scene bg citysidewalk
                                                                show bryant normal at left
                                                                show hobo normal at right
                                                                e "That's the end for you, you dirty beggar"
                                                                e "DIE!"
                                                                play music "gunshot.wav"
                                                                show bryant animated at left
                                                                pause
                                                                stop music
                                                                play music "main.ogg"
                                                                jump apartmentn2
                                                            "Give the hobo a blank stare":
                                                                scene bg citysidewalk
                                                                show bryant gun at left
                                                                show hobo normal at right
                                                                e "..."
                                                                show bryant normal at left
                                                                e "I can't..."
                                                                e "I just can't do it..."
                                                                e "I love you hobo!"
                                                                e "Everyday I pass by you,I just love your smell."
                                                                e "I'm just attracted to your sexy sexiness, I need you in my life!"
                                                                h "..."
                                                                h "Fuck you man."
                                                                jump map2
                                                                
                                                            
                                                        
                                                        show boss normal at offscreenright with move

                                                        e "Oh, hey, I’m alive. How bout that."

                                                        g2 "You got lucky, kid; not many get away so lightly with insultin' the boss."

                                                        e "It won’t happen again."

                                                        g "Damn right."
                                                        
                                                        jump nightclubmenu12




                                                label nightclub_4_32:
                                                        e "I think we should all just calm down, and settle our differences with a peaceful discus-"
                                                        play sound "punch.ogg"
                                                        show bryant punch at center
                                                        

                                                        mb "Never bring a fist to a gunfight, kid. Waste him, boys!"
                                                        play music "gunshot.wav"
                                                        show gangster animated
                                                        show gangster2 animated
                                                        pause
                                                        stop music 
                                                        play music "main.ogg"
                                                        scene bg death
                                                        pause
                                                        jump choice0_done



                                                label nightclub_4_42:
                                                        e "Uhhh, you're lookin' pretty cool, actually. Going for the whole Capone thing, right?"

                                                        mb "Yeah, got these duds a few weeks ago. Felt like I had a business based on his style, why not imitate the guy, right? He was an inspiration."

                                                        e "Yeah…it suits you."

                                                        mb "Thank you. It’s nice to see new kids that have heard of the glorious Capone. You know what, I ain’t gonna kill ya, kid. I’ll be the bigger man this time."

                                                        e "Gee, thanks."

                                                        mb "Enjoy yourself."
                                                        show boss normal at offscreenright with move

                                                        e "Wow, I’m alive after accidentally insulting a mob boss."
                                                        e "Now, moving on to leaving this nightclub alive."
                                                        jump nightclubmenu12




                                                label nightclub_4_52:
                                                        e "Hold it right there, “boss”. I’m actually a cop, and we’ve been lookin' for you for a long time."

                                                        "…"

                                                        "…"

                                                        e "That’s right, you’re all busted. Just hand over your weapons and I’ll-"
                                                        play music "gunshot.wav"
                                                        show gangster animated
                                                        show gangster2 animated
                                                        pause
                                                        scene bg death
                                                        stop music
                                                        play music "scary_music.ogg"
                                                        pause
                                                        jump choice0_done












                                            label nightclub_52:
                                                    g "The boss? Talkin bout the “new boss”?"

                                                    e "Eh? New boss?"

                                                    g "Yeah man, he came outa nowhere and declared himself the new king, or something."
                                                    g2 "Knocked the old boss out cold with voodoo magic or something, man. Freaky stuff."

                                                    e "He sounds like the guy I want."

                                                    g "Really? You must have balls of steel man, cuz he’s wack."

                                                    show magicianyellow normal at offscreenright
                                                    show magicianyellow normal at right with move

                                                    m2 "See, what are you boys yammerin' about, see?"

                                                    g2 "Oh, shit! Boss! We didn’t mean nothing!"

                                                    m2 "Damn right, ya didn’t, see? And don’t you boys worry, I ain’t here for you, see?"
                                                    m2 "I’m here for that guy der, see?"

                                                    e "You knew I was coming?"

                                                    m2 "I could feel the power, see? The power of the hats is no joke kid, see? You stick out like a sore thumb, see?"
                                                    
                                                    e "What are you doing here? This place doesn’t seem very magician-like."

                                                    m2 "I figure yer all wastin' yer time, playin' around by yourselves, see? Since domination spells like the one you got don’t work, see, I figure I’ll just control ya the good ol fashin way, see, with intimidation and threat of force, see?"

                                                    e "Why do you keep saying see?"

                                                    m2 "Cuz I’m a boss now, see? I’ve read up on your dialect, see, blend right in, don’t I, see?"

                                                    e "What, you watched a bunch of classic mobster movies or something?"

                                                    m2 "…Shut up, see?"

                                                    e "Whatever. I came for your hat, which you can probably tell by now."

                                                    m2 "I see, see? Think you can just wipe out all us magicians and get away with it,see?"

                                                    e "What? No, I just asked them for their hats and they had me pass a test for-"

                                                    m2 "I ain’t fallin' for it, see? Probably knocked ‘em out cold when they weren’t lookin, see? Us magicians are most vulnerable to physical violence, see?"
                                                    e "Uh, so is everyone else."

                                                    m2 "Of course, see? So that means you are too, see?"
                                                    m2 "And you’re here in my new domain, see? With my new armed henchmen here to protect me, see?"

                                                    e "… Now that you mention it…"

                                                    m2 "See, see? You were foolish to come here, mortal, see?"
                                                    m2 "Now, boy, prepare to die, see?!? Get him, boys, see!?!"
                                                    play music "gunshot.wav"
                                                    show gangster animated
                                                    show gangster2 animated

                                                    "OH SHIIII-"

                                                    "*Dodging bullets*"
                                                    stop music
                                                    play music "main.ogg"
                                                    show gangster angry
                                                    show gangster2 angry

                                                    e "…Oh, hey, I’m alive."

                                                    g "Oh, crap boss! He just pulled some matrix shit!"
                                                    g2 "Whoa, he’s showin' more mojo than you do!"

                                                    m2 "…Just a fluke, see? I was goin' easy on him, see?"

                                                    g2 "Eh, boss, we were the ones shootin-"

                                                    m2 "Well shoot again, see?!? Keep doin it until you run out of ammo, see!?!"
                                                    play music "gunshot.wav"

                                                    show gangster animated
                                                    show gangster2 animated
                                                    "*Dodging even more bullets*"
                                                    play music "main.ogg"
                                                    show gangster normal
                                                    show gangster2 normal

                                                    m2 "Wow, that was pretty badass."
                                                    m2 "…see."

                                                    e "Yeah, can you, like, stop shooting me?"

                                                    g "Uh, priest guy, we’re all outta ammo!"

                                                    m2 "…"
                                                    m2 "So, what did you want again, mortal? I suppose I’ll deign to hear you out."

                                                    e "Your hat. That curse is lethal, so I need your hat to reverse it."

                                                    m2 "Oh, right, I suppose it did have that side effect."
                                                    m2 "…Uh, I suppose, uh, I’m generous enough, erm, to comply with your request."
                                                    hide magicianyellow
                                                    show magician normal at right
                                                    $ hat += 1
                                                    m2 "And, uh, actually, I was just planning on leaving, see? Uhhh…"

                                                    e "As long as I have your hat, I don’t care anymore."
                                                    e "Actually, where’s the last guy? The one with the red hat."

                                                    m2 "Eh, him? He’s always down by the cemetery, practicing new spells and such."

                                                    e "Right. I’ll just punch him in the face or something while he’s casting, get the last hat, and reverse this shitty curse."
                                                    e "Oh, you can go now if you want, I guess."

                                                    m2 "…Right, then."
                                                    m2 "Mortals are actually pretty scary…"
                                                    show magicianyellow normal at offscreenright with move

                                                    e "And you guys?"

                                                    g "Woah, dog, you Neo or something, we ain’t gonna mess with you."
                                                    g2 "Yeah, man, those were some sweet moves, brah."

                                                    e "Oh, all “cool” now after unloading all your ammo at me eh?"

                                                    g "Ay man, he was threatenin us with all his voodoo shit, man, cut us some slack."
                                                    g2 "Yeah, now that you scared him off we’re Capone’s crew again, wherever he is."
                                                    g "Voodoo guy gave him a nasty ass cold, brutha. Sick shit, literally."
                                                    
                                                    e "Well, enjoy yourselves I guess. I’m going to go home and have a nervous breakdown about what just happened."
                                                    
                                                    g "Peace out, dog."
                                                    g2 "Yeah, come back anytime. We’ll hang with ya."

                                                    e "Yeah… maybe."
                                                    jump apartmentn2




                                            label nightclub_62:
                                                    e "Hold it, “dawgs”, I’m an undercover cop!"
                                                    e "You’re all under arrest! Drop your weapons and put your hands in the a-"
                                                    play music "gunshot.wav"
                                                    show gangster animated
                                                    show gangster2 animated
                                                    pause
                                                    stop music 
                                                    play music "scary_music.ogg"
                                                    scene bg death
                                                    pause
                                                    jump choice0_done


                                                                            

                                                

                                elif result == "policestation":
                                    scene bg policestation
                                    show bryant normal at right
                                    show policeman normal at left
                                    e "Ok, I’m at the police station. Now what?"
                                    p "Hello there, sir. Can I help you with something?"
                                    label pschoice2:
                                        scene bg policestation
                                        show policeman normal at left
                                        show bryant normal at right
                                        menu:
                                            "Go back outside":
                                                e "No thanks, I’m good."
                                                jump map2
                                            "Turn yourself in":
                                                jump choice8_turnin2
                                            "Ask about magicians":
                                                jump choice8_ask2
                                            "Ask for a gun":
                                                jump choice8_gun2
                                            "Report a crime":
                                                jump choice8_report2
    
                                        label choice8_turnin2:
                                            e "I’d like to turn myself in."
                                            p " Oh, my. For what?"
                                            menu:
                                                "Take it back":
                                                    jump choice9_takeitback2
                                                "Wasting time":
                                                    jump choice9_time2
                                                "Being too sexy":
                                                    jump choice9_sexy2
                                                "Attempted murder":
                                                    jump choice9_murder2
                                                "Littering":
                                                    jump choice9_littering2
                                            label choice9_takeitback2:
                                                e "Haha, just kidding."
                                                show policeman angry at left
                                                p "Please don’t joke like that, sir. Sometimes we actually do get the occasional guilty fellow that warrants attention."
                                                e "You’re right... Sorry."
                                                p "Anything else?"
                                                jump pschoice2
                                            label choice9_time2:
                                                e "For wasting an officer’s time."
                                                p "Eh?"
                                                p "..."
                                                p "Oh... I get it. Hah."
                                                p "We made a new law yesterday."
                                                p "If the officer laughs about it, you’re free to go."
                                                e "Well, good for me."
                                                p "Indeed. Seriously, though, do you need anything?"
                                                jump pschoice2
                                            label choice9_sexy2:
                                                e "I’m just too hot, officer."
                                                p "Excuse me?"
                                                e "It should be illegal to look as good as I do. My guilty conscience can no longer tolerate how unfairly distracting I am to the opposite sex."
                                                show policeman angry at left
                                                p "Sir, stop. Please."
                                                e "What do you mean? I’m already on the most-wanted list of every lady in town."
                                                p "Sir, I’m warning you..."
                                                e "Cage me, officer. That is, if you think mere bars of iron can contain this godly form."
                                                
                                                p "Sir, stop, or I will shoot."
                                                e "Fine."
                                                p "... Anything else?"
                                                jump pschoice2
                                            label choice9_murder2:
                                                e "I tried to murder someone."
                                                p "Who?"
                                                e "Uhhh... ummm... That hobo whose been begging for money daily. I beat him within an inch of his life."
                                                p "Oh, just him? Don’t worry. That ungrateful little... I gave him 5$ just to shut him up one day and he called me a cheapskate. Almost pulled my gun out on him right then and there."
                                                e "Wait, what? You are a real police officer, correct?"
                                                p "Yeah, yeah. I'm just saying that you’re in good company."
                                                p "Just between you and me, everyone here at the force wouldn’t look too deeply into it if he went missing. If you know what I mean..."
                                                e "You can’t be serious..."
                                                p "Just putting it out there. Is there anything else on your mind?"
                                                jump pschoice2
                                            label choice9_littering2:
                                                e "I littered."
                                                e "..."
                                                e "I threw a bottle, like, right next to the sign that said $100 fine for littering, when no one was looking."
                                                p "... And you’re actually asking to be arrested for this?"
                                                e "Yes. I committed a crime and I need to be punished."
                                                p "Uh, as long as you feel sufficiently guilty about i-"
                                                e "NO. Punish me!"
                                                p "Er... Right. If you can’t pay the $100 fine, I guess I’ll have no choice but to bring you in."
                                                menu:
                                                    "Pay":
                                                        jump choice10_pay2
                                                    "Don't pay":
                                                        jump choice10_nopay2
                                                    "Bribe him":
                                                        jump choice10_bribe2
                                                label choice10_pay2:
                                                    if (money >= 100):
                                                        $ money -= 100
                                                        e "Here’s your money, you capitalist pig."
                                                        p "Excuse me, sir?"
                                                        e "You heard me, thief. $100 for littering? It's disgusting how our country tolerates such a corrupt system of organized extortion."
                                                        p "Sir, you just-"
                                                        p "..."
                                                        p "Nevermind..."
                                                        e "What was that?"
                                                        p "Nothing, sir. Now that that’s all sorted out, is there anything else you need?"
                                                        jump pschoice2
                                                    else:
                                                        e "I’ll pay the fi-"
                                                        e "Oh wait, I don’t have enough money on me."
                                                        p "So you don’t have enough to cover the fine?"
                                                        e "Nope."
                                                        p "I guess we’ll have to arrest you then."
                                                        e "Yeah, it seems so."
                                                        p "For a $100 fine, I’d say an overnight stay in a cell should do it."
                                                        jump map2
                                                label choice10_nopay2:
                                                    e "I have no funds to cover the cost of my heinous crimes. I must be incarcerated."
                                                    p " ... Ok then, I guess we’ll hold you in one of our cells overnight."
                                                    e "Yes, very good. A long night in a cold damp cell oughta sort me out."
                                                    p "Sir, is there any reason you’re doing this?"
                                                    e "Doing what?!?"
                                                    p "... Nevermind. Follow me."
                                                    scene bg jail
                                                    show bryant normal at left
                                                    show policeman normal at right
                                                    "*Hours later*"
                                                    p "You’re free to go."
                                                    e "WHAT? It hasn’t been a full day yet. I haven’t learned my lesson."
                                                    p "Uh, we’re letting you out early for good behavior."
                                                    e "Oh, this is bullcrap. I’m getting released early after pleading guilty to a crime. I’ll get spoiled under such a lax system. I’ll start considering murder next!"
                                                    p "Sir, none of us here at the force can understand why you’re doing this. Please. Just go home."
                                                    e "NO. PUNISH ME."
                                                    p "Sir, get out."
                                                    e "Such a weak system... Soft on crime... They should bring back the death penalty... grumble grumble."
                                                    e "I’ll be back here, you’ll see! You’ll wish you shot me down here and now."
                                                    p "I do, sir. Now, go back home."
                                                    jump apartmentn2
                                                label choice10_bribe2:
                                                    if (money >= 200):
                                                        $ money -= 200
                                                        e "Woah. Hey now officer, don’t be so hasty."
                                                        e "How’s about I just give you this brand new $100 bill, and you look the other way?"
                                                        p "..."
                                                        p "Sir, are you trying to bribe me?"
                                                        e "Wow, what a smart guy. You saw right through me. Tell ya what, I’ll throw in another hundred. What do you think?"
                                                        p "Sir..."
                                                        p "..."
                                                        p "Uh... Ok then, I guess $200 will do it."
                                                        e "Here you are, officer. Smart man. This will blow over quick, don’t you worry. I’ll keep my head down from now on... Maybe I'll move outta town."
                                                        p "Uh... yeah... You do that."
                                                        p "Um, anything else?"
                                                        jump pschoice2
                                                    else:
                                                        e "Woah. Hey now officer, don’t be so hasty."
                                                        e "How’s about I just give you this brand new $100 bill, and you look the other way?"
                                                        p "..."
                                                        p "Sir, are you trying to bribe me?"
                                                        e "Wow, what a smart guy. You saw right through me. Tell ya what, I’ll throw in another hundred, whatdayasay?"
                                                        p "... Is this a test? Am I being watched?"
                                                        e "No ones gonna know, officer. I ain’t no rat."
                                                        p "No way. Forget it. Just keep your money and go away."
                                                        e "That works too, I guess."
                                                        p "Then... uh... Anything else?"
                                                        jump pschoice2
                                        label choice8_ask2:
                                            e "I’m looking for a bunch of weirdos in silly hats. Have you heard of anyone like that?"
                                            
                                            if(hat > 0):
                                                p "Yeah, but he left awhile ago."
                                                p "Anything else?"
                                                jump pschoice2
                                                
                                            if choice8b:
                                                p "Actually, we just got a person like that holed up in custody."
                                                p "He was yelling gibberish about dolls and the lack of customer service at a self-serve gas pump while trying to fill up some sort of water bottle."
                                                p "Is he a friend of yours?"
                                                e "Erm, an acquaintance. Kind of."
                                                p "Good enough. I’ll bring you to him."
                                                scene bg jail
                                                show magiciangreen normal at right
                                                show bryant normal at left
                                                m4 "-and my sundial doesn’t even work in here! How am I supposed to tell when second breakfast is occurring? Simply outrageous!"
                                                m4 "Oh, it's you. Have you come to deliver the requested tomes?"
                                                e "Do you remember me?"
                                                m4 "Of course. An elephant never forgets, and I, a magician, being at least equal to an elephant in every way, do so as well."
                                                m4 "Wait, what were you here for again?"
                                                label jailchoice2:
                                                    menu:
                                                        "Leave":
                                                            e "Nothing, really. See you later."
                                                            m4 "Oh. Bye. Be sure to get those books soon. You can never stock enough on puppet psychology."
                                                            scene bg policestation
                                                            show bryant normal at right
                                                            show policeman normal at left
                                                            p "Are you done talking with him, then?"
                                                            e "Yep."
                                                            p "Alrighty. Do you need anything else while you’re here?"
                                                            jump pschoice2
                                                        "Ask how he got arrested ":
                                                            jump choice11_how2
                                                        "Punch him in the face ":
                                                            jump choice11_punch2
                                                        "Ask about the curse ":
                                                            jump choice11_curse2
                                                        "Ask for his hat ":
                                                            jump choice11_hat2
                                                    label choice11_how2:
                                                        e "How did an all-powerful magician get arrested?"
                                                        m4 "Eh? All-powerful doesn’t mean all-abusing. They were coming at me with pitiful little guns. It was almost laughable."
                                                        m4 "I feigned surrender just to mock them, and they seemed to realize immediately the difference in our powers."
                                                        m4 "They brought me here, obviously to declare me the new ruler of your country, but the conditions here are just so bare and tasteless."
                                                        m4 "If this is how you treat your soon to be new leader, I can scarcely imagine how you all managed to live so long without starving to death."
                                                        e "That makes two of us."
                                                        m4 "So, soon to be subject, what do you desire of me?"
                                                        jump jailchoice2
                                                    label choice11_punch2:
                                                        play sound "punch.ogg"
                                                        show bryant punch at center
                                                        pause
                                                        show bryant normal at left
                                                        m4 "OW! Owww..."
                                                        e "Who's the all-powerful magician now, asshole?"
                                                        m4 "Urg... Still me of course, I’m just counter casting your physical damage with... uh... a holy mantra. A puppet mantra. Yeah. "
                                                        play sound "punch.ogg"
                                                        show bryant punch at center
                                                        pause
                                                        show bryant normal at left
                                                        m4 "Owwww OWWWW THAT STINGS!!!"
                                                        p "HEY! Are you assaulting the weirdo?"
                                                        e "Oh crap! That’s right... This is still a police station..."
                                                        m4 "HaHA! Yes, my minions, take him away. Lucky you, boy. My curse was almost complete, but I’ll let my new servants punish you in my stead."
                                                        p "Knock it off, tough guy. I don’t know what your deal with him is, but you can cool your jets in a cell for a while."
                                                        e "Aw come on, he deserved it."
                                                        p "The law says otherwise. We’ll let you go at sunset, if you can keep your fists to yourself."
                                                        e "Ugh... Damn cops and their dislike of old fashioned justice..."
                                                        jump apartmentn2
                                                    label choice11_curse2:
                                                        if (knowledge == 0):
                                                            e "Did you curse me?"
                                                            m4 "Hm? You? Yeah."
                                                            e "Well, what the hell!"
                                                            m4 "You were being very disrespectful, you know. We all thought this would be the best way for you to learn."
                                                            e "But now I keep doing unnatural things for no apparent reason!"
                                                            m4 "Well, now you know how a puppet feels when some newbie jerks him around by the strings till he breaks. It sucks, doesn't it?"
                                                            e "Well, undo it!"
                                                            m4 "Nope. Not until you learn to show puppets a little more respect for what they’ve been through. It’ll wear off on its own anyways, quit being a baby about it."
                                                            jump jailchoice2
                                                        else:
                                                            e "You brainwashed me! Now I have to do whatever some unknown force tells me to do."
                                                            m4 "Actually we found out about the whole “unknown force thing”."
                                                            m4 "Turns out all the orders were coming from those jerks who made the stonehenge. "
                                                            m4 "Those \"White Knight\" pricks didn’t like spells that enslaved the general populace, so they jinxed all the good curses to make it so they got the control instead of us."
                                                            m4 "So we just started mass enslaving people till they were so overflowed with orders that they just stopped caring about how good they were being."
                                                            m4 "It's still a loss, since we can’t have human puppets anymore, but at least we annoyed them."
                                                            e "So how is this supposed to show me how it feels to be a puppet?"
                                                            m4 "Oh. Uhhh..."
                                                            m4 "Well you’re still under someone else's control, aren’t you?  Sucks, don’t it?"
                                                            e "Yeah, I guess."
                                                            m4 "Well thats how a puppet feels... Like every day. Tough it out, wimp. Show some respect."
                                                            jump jailchoice2
                                                    label choice11_hat2:
                                                        m4 "Eh? Why?"
                                                        if (knowledge < 2):
                                                            e "Um, uhhh..."
                                                            e "Cuz I think green suits me better?"
                                                            m4 "First you’re dissing the puppets, now you think I’ll give my hat away so easily?"
                                                            e "Come on, you already have a mask... How much headwear do you need? You’ll still look plenty weird without it, don't worry."
                                                            m4 "Go away, or I shall curse you a second time."
                                                            jump jailchoice2
                                                        else:
                                                            e "I need your hats, or your curse will kill me, remember?"
                                                            m4 "Eh? What do you-"
                                                            m4 "Ohhhh... Oh right. THAT."
                                                            m4 "Forgot about that."
                                                            e "You just “forgot” about a curse being lethal?"
                                                            m4 "Well, it's just a minor side-effect. Barely worth mentioning in most cases."
                                                            e "What?!?"
                                                            m4 "Uh, not in this case, I suppose. At least on your end."
                                                            e "So come on, hand over the hat."
                                                            m4 "Wait, I can’t just “hand over the hat” for a minor mistake. Come on now."
                                                            m4 "It's my pride and joy. I’ve been wearing it since my first act of puppeteering. I had my first puppet put it on my head for me! Oh, the memories..."
                                                            e "I’m going to die if I don’t have it! Or can you undo the curse somehow?"
                                                            m4 "I can’t undo it at this point, and I can’t just give the hat away for free..."
                                                            m4 "How’s about you earn it first?"
                                                            e "Earn it?"
                                                            m4 "Yeah, how about a three-question quiz?"
                                                            m4 "The curse was to teach you how a puppet feels; more about our wonderful wizarding culture."
                                                            m4 "If you prove you’ve learned something, I’ll help undo the curse by giving you my hat."
                                                            e "Your wizarding culture? You curse people for the most minor slights and apparently value your hat more than my life."
                                                            m4 "Wow, you actually just answered two of the questions I was about to ask you."
                                                            m4 "..."
                                                            m4 "The final question then: What less famous group did us puppeteers originally diverge from?"
                                                            menu:
                                                                "Leave":
                                                                    jump choice12_leave2
                                                                "I don’t know":
                                                                    jump choice12_dunno2
                                                                "Alchemists":
                                                                    jump choice12_alchemists2
                                                                "Witches":
                                                                    jump choice12_witches2
                                                                "Punch him and take the hat":
                                                                    jump choice12_punch2
                                                            label choice12_leave2:
                                                                e "Nevermind, there’s something else I have to do."
                                                                m4 "Eh? Aren’t you going to die without my hat? It's just a simple quiz."
                                                                e "I’ll be back for it, don’t worry."
                                                                scene bg policestation
                                                                show bryant normal at left
                                                                p "Done talking with him?"
                                                                e "For now."
                                                                p "Well then, anything else you need before you go?"
                                                                jump pschoice2
                                                            label choice12_dunno2:
                                                                e "I don’t know, just give me the hat."
                                                                m4 "Nope, sorry. Can’t just give away my precious hat for no reason, it’d shame my wizarding name."
                                                                e "Come on, I’m going to die without it!"
                                                                m4 "Well, you deserve to, if you can’t even answer such a simple question."
                                                                m4 "I would think it’d be common sense by now. Education nowadays, I bet they aren’t even teaching AP puppeteering anymore."
                                                                m4 "Hmph. Well then, I refuse to surrender my hat. Deal with it. Hmph."
                                                                jump jailchoice2
                                                            label choice12_alchemists2:
                                                                e "Alchemists, right?"
                                                                m4 "Yeah, that’s right. We had to learn to turn stone into gold before we moved on to useful things like making puppets dance."
                                                                m4 "Well, it seems to me like you’ve learned a lot about being a puppet since we’ve cursed you, so I’ll do my part in helping you break it off early."
                                                                m4 "Take my hat, and keep it well."
                                                                hide magiciangreen
                                                                show magician normal at right
                                                                $ hat += 1
                                                                e "Great, one down, three to go!"
                                                                e "Speaking of which, I still need your friends' hats. Do you know where they are?"
                                                                m4 "I’m not sure, they’ve kept me here as ruler for so long that I can’t say I do."
                                                                m4 "Actually, I remember the blue hat guy raving about some type of food source you humans eat, so you’ll probably find him eating somewhere."
                                                                e "\"Blue hat guy\"? You don’t know his name?"
                                                                m4 "Not really."
                                                                m4 "They just drag me around everywhere, and I follow out of peer-pressure."
                                                                m4 "(They’re kinda weirdos, between you and me.)"
                                                                m4 "Anyway, he’ll probably want you to prove yourself to him too, so just explain things to him and prepare to do another quiz or something."
                                                                e "It’s getting late, so I’ll be heading home first. Thanks for the hat, green hat guy."
                                                                m4 "Go forth, young lad, and with your newfound respect for puppets you will surely earn your life back."
                                                                m4 "Meanwhile, I suppose I can tolerate serving as your new ruler for a while, at least till I grow too bored."
                                                                e "Right. You do that."
                                                                jump apartmentn2
                                                            label choice12_witches2:
                                                                e "Witches?"
                                                                m4 "Wit- WHAT?"
                                                                e "Those witches they hunted back in the 1600’s, right? The Salem trials, or whatever they were?"
                                                                m4 "Oh hell no, we’ve had and will have nothing to do with those disgusting mockeries. You’re trying to mock me, aren't you?"
                                                                e "No, I really don’t care. Just give me the hat, dammit."
                                                                m4 "No! If you haven’t learned anything, then I’m not helping you break the curse! Hmph."
                                                                jump jailchoice2
                                                            label choice12_punch2:
                                                                e "Heres what I think of your stupid quiz!"
                                                                play sound "punch.ogg"
                                                                show bryant punch at center 
                                                                pause
                                                                show bryant normal at left
                                                                m4 "OW! Owww..."
                                                                e "Who's the all powerful magician now, asshole? Now hand over the hat already!"
                                                                m4 "Urg... attacking a humble magician in his blind spot. Do you humans have no honor? You totally fail the quiz, by the way. That answer was nowhere near."
                                                                e "Your blind spot? I punched you in the face."
                                                                m4 "You think I can see out of this mask? It doesn’t have eye holes, fool."
                                                                show policeman angry at offscreenright
                                                                show policeman at center with move
                                                                p "HEY. Are you assaulting him?"
                                                                e "Oh crap! That’s right, this is still a police station."
                                                                m4 "Ah yes, guards! Take him away, to wherever you bring people who fail simple quizzes!"
                                                                p "Knock it off, tough guy. I don’t know what your deal with him is, but you can cool your jets in a cell for a while."
                                                                e "Aw come on, he deserved it."
                                                                p "The law says otherwise. We’ll let you go at sunset, if you can keep your fists to yourself."
                                                                e "Ugh... Damn cops and their dislike of old fashioned justice..."
                                                                jump apartmentn2
                                        label choice8_gun2:
                                            e "Can I have a gun?"
                                            p "You mean a permit?"
                                            e "No, just borrow a gun."
                                            e "..."
                                            e "I’ll only need it for like 5 minutes, there’s this guy outside who-"
                                            p "No. Just no."
                                            p "Do you ACTUALLY need anything from us, sir?"
                                            jump pschoice2
                                        label choice8_report2:
                                            e "I’d like to report a crime."
                                            p "Yes?"
                                            e "A group of wizards cursed me. Now I’m forced to do whatever an unknown force wills me to do."
                                            p "..."
                                            p "Sir, that’s not funny. We get actual reports here, we don’t have time to joke around like that."
                                            e "But it really happened!"
                                            e "(Well of course they don’t believe it. I guess I’ll have to solve this problem myself.)"
                                            p "Just don’t joke around like that. Do you really need something here?"
                                            jump pschoice2
                                            
                                            
                                                                
                                                                
                                                                
                                                                
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                        
                                                        
                                                         
                                                        
                                                        
                                                        
                                                        
                                                
                                                
                                            
                                            
                                                        
                                                         
                                                         
                                                        
                                                        
                                                        
                                                        


                                                    
                                                    
                                                    
                                                        
                                                        
                                                        
                                                        
                                                        
                                                    
                                                    
                                                        
                                                
                                                

                                                
                                                
                                                
                                                
                                                
                                                
                                            
                                        
                                    
                                        
                                            
                                    
                                return
                        
                                pause
                                jump choice0_done
    label choice0_done:
#        python:
 #           renpy.free_memory()
  #          success = maze.main()
            
   #     if success == 1:
    #        e "Yes! I got it!"
     #   elif success == 0:
      #      e "Aww... I ran out of time..."
       # else:
        #    e "Nobody likes a quitter..."
         #   $ renpy.quit()
            
            
    
    

   
    #python:
        #success = maze.main()

#label startMaze:
    #$ renpy.free_memory()
    #$ success = maze.main()
    #$ renpy.pause(.1)
    

