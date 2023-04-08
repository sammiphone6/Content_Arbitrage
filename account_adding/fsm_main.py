from fsm_functions import facebook_pairing_script, insta_creation_script


####################
# FOR INSTAS: Make sure tempPFPs is the default folder
# FOR BOTH: Make sure Nord is set up to the right as needed (with France to US in view)
# FOR BOTH: Make sure no pages to the right of the safari/nord split page
# FOR BOTH: Make sure to record screen
####################

types = [
    'insta',
    # 'facebook',
]

if 'insta' in types: insta_creation_script()
if 'facebook' in types: facebook_pairing_script()