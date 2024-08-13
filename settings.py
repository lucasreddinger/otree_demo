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
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'payment_info'],
        num_demo_participants=3,
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='appcopy',
        display_name='appcopy: Sandwich design (App A -> App B -> App A)',
        num_demo_participants=1,
        app_sequence=['appcopy1', 'multi_select', 'appcopy2'],
    ),
    dict(
        name='are_you_sure',
        display_name="are_you_sure: 'Are you sure?' popup based on the user's input",
        num_demo_participants=1,
        app_sequence=['are_you_sure'],
    ),
    dict(
        name='audio_alert',
        display_name="audio_alert: Audio alert (speak some text to get the participant's attention, after a wait page)",
        num_demo_participants=2,
        app_sequence=['audio_alert'],
    ),
    dict(
        name='back_button',
        display_name='back_button: Back button for multiple instructions pages',
        num_demo_participants=1,
        app_sequence=['back_button'],
    ),
    dict(
        name='balance_treatments_for_dropouts',
        display_name='balance_treatments_for_dropouts: Assign a player to the treatment with the fewest datapoints',
        num_demo_participants=6,
        app_sequence=['balance_treatments_for_dropouts'],
    ),
    dict(
        name='bmi_calculator',
        display_name='bmi_calculator: Basic 1-player game (BMI calculator)',
        num_demo_participants=1,
        app_sequence=['bmi_calculator'],
    ),
    dict(
        name='chat_from_scratch',
        display_name='chat_from_scratch: Chat implementation from scratch (easier to customize)',
        num_demo_participants=3,
        app_sequence=['chat_from_scratch'],
    ),
    dict(
        name='chat_with_experimenter',
        display_name='chat_with_experimenter: Chat with experimenter',
        num_demo_participants=1,
        app_sequence=['chat_with_experimenter'],
    ),
    dict(
        name='complex_form_layout',
        display_name='complex_form_layout: Complex form layout',
        num_demo_participants=1,
        app_sequence=['complex_form_layout'],
    ),
    dict(
        name='comprehension_test_complex',
        display_name='comprehension_test_complex: Comprehension test (quiz you must pass to proceed)',
        num_demo_participants=1,
        app_sequence=['comprehension_test_complex'],
    ),
    dict(
        name='comprehension_test_simple',
        display_name='comprehension_test_simple: Comprehension test (simple version)',
        num_demo_participants=1,
        app_sequence=['comprehension_test_simple'],
    ),
    dict(
        name='configurable_players_per_group',
        display_name="configurable_players_per_group: Configurable players_per_group (doesn't work in demo mode)",
        num_demo_participants=12,
        app_sequence=['configurable_players_per_group'],
        players_per_group=3,
    ),
    dict(
        name='constant_sum',
        display_name='constant_sum: Constant-sum input (3 numbers that add up to 100)',
        num_demo_participants=1,
        app_sequence=['constant_sum'],
    ),
    dict(
        name='count_button_clicks',
        display_name='count_button_clicks: Count button clicks',
        num_demo_participants=1,
        app_sequence=['count_button_clicks'],
    ),
    dict(
        name='css',
        num_demo_participants=1,
        app_sequence=['css'],
        display_name='css: CSS to style timer and chat box',
    ),
    dict(
        name='custom_export_groups',
        display_name='custom_export_groups: custom_export: 1 row for each group',
        num_demo_participants=4,
        app_sequence=['custom_export_groups'],
    ),
    dict(
        name='detect_mobile',
        display_name='detect_mobile: Block mobile browsers',
        num_demo_participants=1,
        app_sequence=['detect_mobile'],
    ),
    dict(
        name='dropout_detection',
        display_name='dropout_detection: Dropout detection for single-player game',
        num_demo_participants=1,
        app_sequence=['dropout_detection'],
    ),
    dict(
        name='dropout_end_game',
        display_name='dropout_end_game: Dropout detection for multiplayer game (end game if has dropout)',
        num_demo_participants=2,
        app_sequence=['dropout_end_game', 'placeholder'],
    ),
    dict(
        name='experimenter_input',
        app_sequence=['experimenter_input'],
        display_name='experimenter_input: Experimenter input during the experiment (e.g. entering a random drawing)',
        num_demo_participants=2,
    ),
    dict(
        name='factorial_treatments',
        display_name='factorial_treatments: Factorial balanced treatment design',
        num_demo_participants=16,
        app_sequence=['factorial_treatments'],
    ),
    dict(
        name='gbat_fallback_smaller_group',
        display_name='gbat_fallback_smaller_group: group_by_arrival_time: fall back to a smaller group if not enough people show up',
        num_demo_participants=4,
        app_sequence=[
            'gbat_fallback_smaller_group_part0',
            'gbat_fallback_smaller_group_part1',
        ],
    ),
    dict(
        name='gbat_fallback_solo_task',
        display_name='gbat_fallback_solo_task: group_by_arrival_time: skip the multiplayer task if no other players show up',
        num_demo_participants=2,
        app_sequence=[
            'gbat_fallback_solo_task_part0',
            'gbat_fallback_solo_task_part1',
            'gbat_fallback_solo_task_part2',
        ],
    ),
    dict(
        name='gbat_keep_same_groups',
        display_name='gbat_keep_same_groups: group_by_arrival_time: Preserve same groups as a previous app that used group_by_arrival_time.',
        num_demo_participants=6,
        app_sequence=[
            'gbat_keep_same_groups_part0',
            'gbat_keep_same_groups_part1',
            'gbat_keep_same_groups_part2',
        ],
    ),
    dict(
        name='gbat_new_partners',
        display_name='gbat_new_partners: group by arrival time, but in each round assign to a new partner.',
        num_demo_participants=16,
        app_sequence=['gbat_new_partners'],
    ),
    dict(
        name='gbat_treatments',
        display_name='gbat_treatments: group_by_arrival_time and group-level treatments',
        num_demo_participants=6,
        app_sequence=['gbat_treatments'],
    ),
    dict(
        name='gbat_treatments_complex',
        display_name='gbat_treatments_complex: group_by_arrival_time and group-level treatments (complex version)',
        num_demo_participants=6,
        app_sequence=['gbat_treatments_complex'],
    ),
    dict(
        name='getattr_setattr',
        display_name='getattr_setattr: getattr() to access numbered fields like player.num1, player.num2, ..., player.num9',
        num_demo_participants=1,
        app_sequence=['getattr_setattr'],
    ),
    dict(
        name='groups_csv',
        display_name='groups_csv: Assign players to groups defined in a CSV file',
        num_demo_participants=6,
        app_sequence=['groups_csv'],
    ),
    dict(
        name='history_table',
        display_name='history_table: History table',
        num_demo_participants=1,
        app_sequence=['history_table'],
    ),
    dict(
        name='image_choices',
        display_name='image_choices: Images in radio button choices',
        num_demo_participants=1,
        app_sequence=['image_choices'],
    ),
    dict(
        name='input_calculation',
        display_name='input_calculation: Immediate calculation so the user can see the potential result of their decision',
        num_demo_participants=1,
        app_sequence=['input_calculation'],
    ),
    dict(
        name='live_volunteer',
        display_name="live_volunteer: Live volunteer's dilemma (first player to click moves everyone forward).",
        num_demo_participants=3,
        app_sequence=['live_volunteer'],
    ),
    dict(
        name='longitudinal',
        display_name='longitudinal: Longitudinal study (2-part study taking place across days/weeks)',
        num_demo_participants=1,
        app_sequence=['longitudinal'],
    ),
    dict(
        name='min_time_on_page',
        display_name='min_time_on_page: Minimum time on a page',
        num_demo_participants=1,
        app_sequence=['min_time_on_page'],
    ),
    dict(
        name='multi_language',
        display_name='multi_language: Translate an app to multiple languages (e.g. English and German)',
        num_demo_participants=1,
        app_sequence=['multi_language'],
    ),
    dict(
        name='multi_page_timeout',
        display_name='multi_page_timeout: Timeout spanning multiple pages',
        num_demo_participants=1,
        app_sequence=['multi_page_timeout'],
    ),
    dict(
        name='multi_select',
        display_name='multi_select: Multi-select widget (a.k.a. multiple choice / multiple answer)',
        num_demo_participants=1,
        app_sequence=['multi_select'],
    ),
    dict(
        name='multi_select_complex',
        display_name="multi_select_complex: Multi-select widget (flexible version with custom labels & 'select at least N')",
        num_demo_participants=1,
        app_sequence=['multi_select_complex'],
    ),
    dict(
        name='other_player_previous_rounds',
        display_name="other_player_previous_rounds: Showing other players' decisions from previous rounds",
        num_demo_participants=8,
        app_sequence=['other_player_previous_rounds'],
    ),
    dict(
        name='pass_data_between_apps',
        display_name='pass_data_between_apps: Pass data between apps',
        num_demo_participants=1,
        app_sequence=['pass_data_between_apps_part1', 'pass_data_between_apps_part2'],
    ),
    dict(
        name='pay_random_app',
        display_name='pay_random_app: Pay a randomly selected app',
        num_demo_participants=2,
        app_sequence=[
            'pay_random_app_multi_player',
            'pay_random_app_single_player',
            'pay_random_app3',
        ],
    ),
    dict(
        name='pay_random_round',
        display_name='pay_random_round: Pay a randomly selected round',
        num_demo_participants=1,
        app_sequence=['pay_random_round'],
    ),
    dict(
        name='persist_raw',
        display_name='persist_raw: Persist raw HTML form inputs on reload (sliders, checkboxes, etc).',
        app_sequence=['persist_raw'],
        num_demo_participants=1,
    ),
    dict(
        name='practice_rounds',
        display_name='practice_rounds: Practice rounds',
        app_sequence=['practice_rounds'],
        num_demo_participants=1,
    ),
    dict(
        name='progress_bar',
        display_name='progress_bar: Progress bar',
        num_demo_participants=1,
        app_sequence=['progress_bar'],
    ),
    dict(
        name='question_with_other_option',
        display_name="question_with_other_option: Menu with an 'other' option that lets you type in a valueInput manually",
        num_demo_participants=4,
        app_sequence=['question_with_other_option'],
    ),
    dict(
        name='questions_from_csv',
        display_name='questions_from_csv: Quiz questions loaded from CSV spreadsheet (complex version)',
        num_demo_participants=2,
        app_sequence=['questions_from_csv_complex'],
    ),
    dict(
        name='questions_from_csv_simple',
        display_name='questions_from_csv_simple: Quiz questions loaded from CSV spreadsheet (simple version)',
        num_demo_participants=2,
        app_sequence=['questions_from_csv_simple'],
    ),
    dict(
        name='quiz_with_explanation',
        display_name="quiz_with_explanation: Quiz + post-quiz explanation. Re-display the previous page's form as read-only, with answers/explanation.",
        num_demo_participants=1,
        app_sequence=['quiz_with_explanation'],
    ),
    dict(
        name='radio',
        display_name='radio: Radio buttons in various layouts, looping over radio choices',
        app_sequence=['radio'],
        num_demo_participants=1,
    ),
    dict(
        name='radio_switching_point',
        display_name='radio_switching_point: Radio button table with single switching point (strategy method)',
        num_demo_participants=1,
        app_sequence=['radio_switching_point'],
    ),
    dict(
        name='random_num_rounds',
        display_name='random_num_rounds: Random number of rounds',
        num_demo_participants=2,
        app_sequence=['random_num_rounds'],
    ),
    dict(
        name='random_num_rounds_multiplayer',
        display_name='random_num_rounds_multiplayer: Random number of rounds for multiplayer (random stopping rule)',
        num_demo_participants=2,
        app_sequence=[
            'random_num_rounds_multiplayer',
            'random_num_rounds_multiplayer_end',
        ],
    ),
    dict(
        name='random_question_order',
        display_name='random_question_order: Randomize order of questions',
        num_demo_participants=4,
        app_sequence=['random_question_order'],
    ),
    dict(
        name='random_task_order',
        display_name='random_task_order: Randomize order of different tasks',
        num_demo_participants=4,
        app_sequence=['random_task_order'],
    ),
    dict(
        name='rank_players',
        display_name='rank_players: Rank players',
        num_demo_participants=4,
        app_sequence=['rank_players'],
    ),
    dict(
        name='rank_topN',
        display_name='rank_topN: Ranking your top N choices from a list of options.',
        num_demo_participants=1,
        app_sequence=['rank_topN'],
    ),
    dict(
        name='rank_widget',
        display_name='rank_widget: Rank/reorder form widget',
        num_demo_participants=1,
        app_sequence=['rank_widget'],
    ),
    dict(
        name='redirect_to_other_website',
        display_name='redirect_to_other_website: Redirect the user to another website and pass their data',
        num_demo_participants=1,
        app_sequence=['redirect_to_other_website'],
    ),
    dict(
        name='save_wrong_answers',
        display_name='save_wrong_answers: Save the history of invalid responses a user made.',
        num_demo_participants=1,
        app_sequence=['save_wrong_answers'],
    ),
    dict(
        name='sequential',
        display_name='sequential: Sequential game',
        num_demo_participants=3,
        app_sequence=['sequential'],
    ),
    dict(
        name='sequential_symmetric',
        display_name='sequential_symmetric: Sequential game (symmetric)',
        num_demo_participants=3,
        app_sequence=['sequential_symmetric'],
    ),
    dict(
        name='slider_graphic',
        display_name='slider_graphic: Slider that changes an image (e.g. happy to sad scale)',
        num_demo_participants=1,
        app_sequence=['slider_graphic'],
    ),
    dict(
        name='slider_live_label',
        display_name='slider_live_label: Slider with live updating label',
        num_demo_participants=1,
        app_sequence=['slider_live_label'],
    ),
    dict(
        name='supergames',
        display_name='supergames: Supergames consisting of multiple rounds each',
        num_demo_participants=1,
        app_sequence=['supergames'],
    ),
    dict(
        name='timer_custom',
        display_name='timer_custom: Timer: replacing the default timer with your own',
        num_demo_participants=1,
        app_sequence=['timer_custom'],
    ),
    dict(
        name='treatments_from_spreadsheet',
        display_name='treatments_from_spreadsheet: Treatments defined in a spreadsheet',
        num_demo_participants=12,
        app_sequence=['treatments_from_spreadsheet'],
    ),
    dict(
        name='wait_for_specific_people',
        display_name='wait_for_specific_people: Wait only for specific people',
        num_demo_participants=8,
        app_sequence=['wait_for_specific_people'],
    ),
    dict(
        name='wait_page_timeout',
        display_name='wait_page_timeout: Timeout on a WaitPage (exit the experiment)',
        num_demo_participants=2,
        app_sequence=['wait_page_timeout'],
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

DEMO_PAGE_INTRO_HTML = """
combined demos: more demos, samples, snippets

https://www.otreehub.com/projects/otree-more-demos/

https://www.otreehub.com/projects/otree-snippets/
"""

DEMO_PAGE_TITLE = "demos"

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
    'app_payoffs',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'quiz_num_correct',
    'selected_round',
    'task_rounds',
    'time_pressure',
    'wait_page_arrival',
]

SESSION_FIELDS = [
    'finished_p1_list',
    'iowa_costs',
    'wisconsin',
    'intergenerational_history',
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
]

