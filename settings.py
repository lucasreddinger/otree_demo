from os import environ

SESSION_CONFIGS = [
    dict(
        name='shop',
        display_name='shop: Shopping app (online grocery store)',
        app_sequence=['shop'],
        num_demo_participants=1,
    ),
    dict(
        name='asynchronous',
        app_sequence=['asynchronous'],
        display_name='asynchronous: Asynchronous 2-player game (no waiting for another player)',
        num_demo_participants=6,
    ),
    dict(
        name='bigfive',
        display_name='bigfive: Big 5 personality test',
        app_sequence=['bigfive'],
        num_demo_participants=1,
    ),
    dict(
        name='bots_vs_humans',
        display_name='bots_vs_humans: Bots playing against a human participant (complex version)',
        num_demo_participants=1,
        app_sequence=['bots_vs_humans_complex'],
    ),
    dict(
        name='bots_vs_humans_simple',
        display_name='bots_vs_humans_simple: Bots playing against a human participant (simple version)',
        num_demo_participants=1,
        app_sequence=['bots_vs_humans_simple'],
    ),
    dict(
        name='choice_list',
        display_name='choice_list: Choice list (Holt/Laury, equivalence test, etc)',
        app_sequence=['choice_list'],
        num_demo_participants=1,
    ),
    dict(
        name='continuous_time_slider',
        display_name='continuous_time_slider: Continuous-time public goods game with slider',
        app_sequence=['continuous_time_slider'],
        num_demo_participants=2,
    ),
    dict(
        name='crazy_eights',
        display_name='crazy_eights: Card game (crazy eights)',
        app_sequence=['crazy_eights'],
        num_demo_participants=2,
    ),
    dict(
        name='dollar_auction',
        app_sequence=['dollar_auction'],
        num_demo_participants=3,
    ),
    dict(
        name='double_auction',
        display_name='double_auction: Double auction market',
        app_sequence=['double_auction'],
        num_demo_participants=4,
    ),
    dict(
        name='ebay',
        display_name='ebay: eBay style auction',
        app_sequence=['ebay'],
        num_demo_participants=3,
    ),
    dict(
        name='fast_consensus',
        display_name='fast_consensus: Fast consensus: Reach a consensus with your group before your payoffs shrink to 0.',
        num_demo_participants=3,
        app_sequence=['fast_consensus'],
    ),
    dict(
        name='go_no_go',
        display_name='go_no_go: Attention test (Go/No-Go)',
        app_sequence=['go_no_go'],
        num_demo_participants=1,
    ),
    dict(
        name='image_annotation',
        display_name='image_annotation: Image annotation',
        app_sequence=['image_annotation'],
        num_demo_participants=1,
    ),
    dict(
        name='image_rating',
        display_name='image_rating: Image rating',
        app_sequence=['image_rating'],
        num_demo_participants=1,
    ),
    dict(
        name='intergenerational',
        app_sequence=['intergenerational'],
        display_name='intergenerational: \n        Intergenerational/evolutionary game, passing along donations to future players, \n        in a chain.',
        num_demo_participants=6,
    ),
    dict(
        name='iowa_gambling',
        display_name='iowa_gambling: Iowa Gambling Task',
        app_sequence=['iowa_gambling'],
        num_demo_participants=1,
    ),
    dict(
        name='live_bargaining',
        display_name='live_bargaining: Live bargaining between 2 players',
        app_sequence=['live_bargaining'],
        num_demo_participants=2,
    ),
    dict(
        name='live_coordination',
        display_name='live_coordination: Live coordination (voting with chat/negotiation)',
        app_sequence=['live_coordination'],
        num_demo_participants=6,
    ),
    dict(
        name='nim',
        display_name='nim: Race game / Nim (take turns adding numbers to reach a target)',
        app_sequence=['nim'],
        num_demo_participants=2,
    ),
    dict(
        name='panas',
        display_name='panas: PANAS (positive and negative affect schedule)',
        app_sequence=['panas'],
        num_demo_participants=1,
    ),
    dict(
        name='punishment',
        display_name='punishment: Public goods with punishemnt',
        app_sequence=['punishment'],
        num_demo_participants=4,
    ),
    dict(
        name='randomize_stimuli',
        display_name='randomize_stimuli: Demo of different stimulus randomizations',
        app_sequence=['randomize_stimuli'],
        num_demo_participants=5,
    ),
    dict(
        name='read_mind_in_eyes',
        display_name='read_mind_in_eyes: Reading the Mind in the Eyes Test (Baron-Cohen et al. 2001)',
        app_sequence=['read_mind_in_eyes'],
        num_demo_participants=1,
    ),
    dict(
        name='rockpaperscissors',
        display_name='rockpaperscissors: Rock/Paper/Scissors',
        app_sequence=['rockpaperscissors'],
        num_demo_participants=2,
    ),
    dict(
        name='scheduling',
        display_name='scheduling: Scheduling players to arrive at the same time',
        num_demo_participants=12,
        app_sequence=['scheduling_part0', 'scheduling_part1'],
    ),
    dict(
        name='strategy_method',
        display_name='strategy_method: Strategy Method',
        app_sequence=['strategy_method'],
        num_demo_participants=2,
    ),
    dict(
        name='supergames_indefinite',
        display_name="supergames_indefinite: Supergames of an indefinitely repeated prisoner's dilemma",
        num_demo_participants=2,
        app_sequence=['supergames_indefinite'],
    ),
    dict(
        name='svo',
        display_name='svo: Social Value Orientation Measure (SVO)',
        app_sequence=['svo'],
        num_demo_participants=1,
    ),
    dict(
        name='tictactoe',
        display_name='tictactoe: Tic-Tac-Toe',
        app_sequence=['tictactoe'],
        num_demo_participants=2,
    ),
    dict(
        name='twitter',
        app_sequence=['twitter'],
        display_name='twitter: Social network (mini-Twitter)',
        num_demo_participants=6,
    ),
    dict(
        name='wait_page_from_scratch',
        display_name='wait_page_from_scratch: Wait page implemented from scratch, using live pages.',
        num_demo_participants=6,
        app_sequence=['wait_page_from_scratch'],
    ),
    dict(
        name='wisconsin',
        display_name='wisconsin: Wisconsin Card Sorting Test',
        app_sequence=['wisconsin'],
        num_demo_participants=1,
    ),
    dict(
        name='word_search',
        display_name='word_search: Word search game (multiplayer)',
        app_sequence=['word_search'],
        num_demo_participants=2,
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1.00, participation_fee=0.00, doc="")

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """
DEMO_PAGE_TITLE = "More demos of oTree (especially using live pages)"

SECRET_KEY = '4387860144726'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = [
    'booking_time',
    'cards',
    'order',
    'reaction_times',
    'read_mind_in_eyes_score',
    'responses',
    'stimuli',
    'svo_angle',
    'svo_category',
]

SESSION_FIELDS = ['finished_p1_list', 'iowa_costs', 'wisconsin', 'intergenerational_history']
