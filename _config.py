mapIcons = [
    ('treePines', (.2, .2), "Forest", True),
    ('rocksMountain', (-.3, -.15), "Mountain", True),
    ('vulcano', (-.4, -.3), "Volcano", True),
    ('lake', (.28, .09), "Lake", True),
    ('houses', (.21, -.24), "Town", True),
    ('waterWheel', (.45, -.09), "Factory", True)
]

manual_btns = {
    'diseases' : [
        ('diseases_main', .44, (-.01, 0),
        '''
            <scale: 1.5><orange>1. Vector Borne Diseases (VBD)<default><scale:1> 
            Vector borne diseases are infections transmitted by the bite of infected 
            <lime>arthropod species<default>, such as mosquitoes, ticks, triatomine bugs, 
            sandflies, and black flies.
            
            <scale: 1.5><orange>2. Water Borne Diseases (WBD)<default><scale:1> 
            Water borne diseases are illnesses caused by <lime>microorganisms<default> in untreated or 
            contaminated water. 
        '''
        ),
        ('west_nile_fever_cropped', .17, (-0.36, -0.15), 
        '''
            About 
            <scale:1.5><lime>68%<default><scale:1> 
            people could be exposed under West Nile virus!!!
        '''),
        ('mosquito', .32, (-0.355, .09),
        '''
            Increased <olive>rainfall<default>, <olive>flooding<default> and <olive>humidity<default> creates more viable areas for 
            <lime>vector breeding<default> (eggs hatch <lime>faster<default> in hotter climates)
        '''),
        ('drinking_water', .145, (0.2, 0.13),
        '''
            Drinking water can be contaminated due to increased frequency and intensity of 
            heavy rainfall (runoff and flooding), especially in <lime>river<default> and <lime>coastal areas<default>
        '''),
        ('pathogens', .15, (0.39, 0.14),
        '''
            Flooding and higher temperatures are likely to <lime>transport pathogens<default> into 
            recreational waters and foster their growth.
        '''),
        ('crops', .29, (0.32, -0.115),
        '''
            <lime>Seafood<default> can also be contaminated with the growth, survival and spread of 
            bacteria, viruses and toxins created by harmful <olive>algae<default>.
        ''')
    ],
    'disaster' : [
        ('drought', .17, (-.36, -.15)),
        ('wildfire', .17, (-.36, -.15)),
        ('tornado', .17, (-.36, -.15)),
        ('eruption', .17, (-.36, -.15)),
        ('floods', .17, (-.36, -.15)),
        ('landslide', .17, (-.36, -.15))
    ],
    'economic' : [
        (),
    ],
    'famine' : [
        ('areas', .17, (-.3, .1),
        '''
            Parts of Yemen, South Sudan and Burkina Faso are the most frustrated. 
            Many Yemenis are facing a death sentence as widespread hunger stalks 
            their nation.
        '''),
        ('population', .17, (.36, .15),
        '''
            About <lime>30 million<default> people are experiencing alarming hunger, 
            severe levels of food insecurity and malnutrition;
            <lime>10 million<default> of them are facing emergency and famine conditions
        '''
        ),
        ('crops', .17, (.36, -.25),
        '''
            Need to produce about 50% more food!
            Combined food loss and waste amount to <lime>25–30%<default> of total food produced.
            Overall food production will decrease <lime>15% to 17%<default>
        '''
        ),
        ('water', .17, (.02, .1),
        '''
            Water availability will <lime>decline<default> as temperature rising: 
            more water to evaporate from both land and oceans; 
            <orange>Yet<default> also, in turn, a warmer atmosphere can hold more water – 
            roughly <lime>4%<default> more water for every 1ºF rise in temperature
        '''
        )
    ]
}

plot_sites = {
    "Hokkaido" : {
        "position" : (.48, .15),
        "plot" : 0
    },
    "Australia" : {
        "position" : (.5, -.22),
        "plot" : "Seaside"
    },
    "South Sudan" : {
        "position" : (0, -.05),
        "plot" : 1
    },
    "Lousiana" : {
        "position" : (-.34, .15),
        "plot" : "Seaside"
    },
    "Amazon" : {
        "position" : (-.32, -.15),
        "plot" : 2
    }
}

game_prompts = {
    "world_map" : '''Choose a site to start your investigation!\n    * Okay.'''
}

# Sea relevant

SEA_info = {
    "oa_effects" : '''
                \nDirect
                \n  <scale: .8>1. Reduced <lime>growth rates<default> of juvenile fish
                \n  2. Increased risk of <lime>predation<default><scale: 1>
                \nFoodweb
                \n  <scale: .8>Nearly collapsed<scale: 1>
                \nSensory
                \n  <scale: .8><lime>Sensory signals<default><scale: .8> are interfered <default><scale: 1>
                \nCumulative
                \n  <scale: .8>Overall <lime>productivity<default> of fish stocks reduced <scale: 1>
                ''',
}

SEA_img = {
    "salmon" : r"assets\pics\hokkaido\salmon.png"
}

SUDAN_tasks = {
    "landuse" : ("Based on the chart, do you think South Sudan is agri-potential?", ("YES", "NO"), 1),
    "constraints" : (
        '''This is a report from a decades before. However, 
        \nthe climate is somewhat worsen today. 
        \nWhich of these constraints do you think are underestimated? 
        \n<light_grey>(Not sure? Check your manual!)<default>
        ''', ("Pests", "Rainfall", "Lack of Water"), 3),
    "potential" : ("We are now planning some more cultivation. What one do you would be the best?", ("Wheat", "Maize", "Tea/Coffee", "Rice", "Soy"), 1)
}

VIRUS_info = {
    'hepatitis_a' :(
        "<scale:2>HEPATITIS A",
        '''
        <scale: 1.5><white>Symptoms: <black><scale:1.2>
        1. Fatigue, Sudden nausea and vomiting, 

        2. Abdominal pain or discomfort and Joint pain. 
        ''',
        '''
        <scale: 1.5><white>Most commonly spreads when:<black><scale:1.2>
        1. Drink contaminated water or swallow contaminated ice, 

        2. Eat raw shellfish harvested from water polluted with sewage, 

        3. Have sex with someone who has the virus 
           even if that person has no signs or symptoms. 
        '''
    ),
    'west_nile' :(
        "<scale:2>WEST NILE",
        '''
        <scale: 1.5><white>Symptoms: <black><scale:1.2>
        Fever, Headache, Joint pains, Vomiting or Diarrhea.
        ''',
        '''
        <scale: 1.5><white>Most commonly spreads when:<black><scale:1.2>
        1. bites from infected mosquitoes. 
            (Mosquitoes become infected when they feed on infected birds,
            which circulate the virus in their blood for a few days.)
         
        2. contact with other infected animals, their blood, 
           or other tissues. 
        '''
    ),
    'lyme' : (
        "<scale:2>LYME DISEASE",
        '''
        <scale: 1.5><white>Symptoms: <black><scale:1.2>
        1. Begin as soon as <lime>30<black> minutes after ingestion:
        itching, numbness of the lips, tongue, hands, and/or feet.
        2. First 6 to 17 hours:
        abdominal cramps, vomiting, diarrhea, and red skin rash (pruritus) 
        
        ''',
        '''
        <scale: 1.5><white>Most commonly spreads when:<black><scale:1.2>
        1.  bite of infected ticks. 
            (Ticks can attach to any part of the human body but are 
            often found in hard-to-see areas (e.g., groin, armpits, scalp)
            
            Most humans are infected through the bites of immature ticks
            (less than 2 mm) called <lime>nymphs<black>. 
        '''
    ),
    'cfp' : (
        "<scale:2>CIGUATERA POISONING",
        '''
        <scale: 1.5><white>Symptoms: <black><scale:1.2>
        Fever, rash, facial paralysis, and arthritis
        ''',
        '''
        <scale: 1.5><white>Most commonly spreads when:<black><scale:1.2>
        1.  Caused by more than <lime>400<black> different species of fish

            High levels in a marine organism that typically inhabits 
            low-lying tropical shore areas and coral reefs. 
            
            As local fish feed on this organism, toxin accumulates in 
            their bodies and ultimately causes CFP when humans 
            consume the fish. 
        '''
    )
}