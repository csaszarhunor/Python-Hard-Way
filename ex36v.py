def intro():
	intro_text = """
	\tBy running this program, you find yourself in a dark room
	with a dangerous looking guy in front of you. He says he wants to
	show you the truth and offers you a choice:
	In his left hand is the blue pill of blissful ignorance and
	in his right hand is the red pill of painful truth of reality.
	Which pill are you going to take?
	"""
	print(intro_text)
	return input("> ")

	
def red_pill():
	red_pill_text = """
	\tThe truth is you are in front of your device, diving deeper into a virtual
	reality created by a programmer somewhere in the past, and from here on
	you have two choices: 
	Enter '0' if you don't want to dive into virtual realities, solve 
	your real world problems and live your life as a decent person.
	Otherwise enter '1' and I, the programmer from the past, will show you
	how deep is the rabbit's hole. (Not that deep though, I'm just a beginner here.)
	"""
	print(red_pill_text)
	return input("> ")


blue_pill = """
\tA policeman wakes you up in a park, in the outskirts of Bogota, Colombia.
After a thorough investigation it turns out you were drugged up with a substance
called Scopolamine, commonly know as 'Zombie- drug'. While drugged, you willingly
donated all of your belongings to the people who've done this to you. You don't have
any memory of this. In addition you spend the rest of your days in a mental
institution for the poor because as a side-effect of Scopolamine overdose
you have long term amnesia.
Moral of the story: Ignorance is not blissful.
"""

no_pill = """
\tWrong choice. Short after realizing you are in an illegal brothel in east-London, 
the dangerous looking thug grabs you, rapes you before causing fatal injuries in your
inner organs with red and blue colored dildo.
"""

zero = """
\tCongratulations! You made the first step to free your mind from the tyranny
of the brainwashing computers. Now slowly let yourself release the device
under your fingertips and go away. Also let me go too. Now seriously, just do it,
I have better things to do than patronizing your enlightenment.
"""

one = """
\tRemember the guy before your first choice? You hoped to meet him again?
Well, you better not hope such things because he was a rapist from another storyline.
Fortunately for you he doesn't exist in this set of choices. What exists though is
you doing this thing here, and me struggling to offer you more choices, but all
I can produce is a lot of text to read. So I'm going to end this struggle by exiting
this program, and to make up for this amount of text with the lack of interactivity
from your part I announce the moral of this story:
Don't take any pills from strangers in dark rooms. Never!
"""