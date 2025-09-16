# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from deadlock-api-client.api.analytics_api import AnalyticsApi
    from deadlock-api-client.api.builds_api import BuildsApi
    from deadlock-api-client.api.commands_api import CommandsApi
    from deadlock-api-client.api.custom_matches_api import CustomMatchesApi
    from deadlock-api-client.api.e_sports_api import ESportsApi
    from deadlock-api-client.api.info_api import InfoApi
    from deadlock-api-client.api.internal_api import InternalApi
    from deadlock-api-client.api.leaderboard_api import LeaderboardApi
    from deadlock-api-client.api.mmr_api import MMRApi
    from deadlock-api-client.api.matches_api import MatchesApi
    from deadlock-api-client.api.patches_api import PatchesApi
    from deadlock-api-client.api.players_api import PlayersApi
    from deadlock-api-client.api.sql_api import SQLApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from deadlock-api-client.api.analytics_api import AnalyticsApi
from deadlock-api-client.api.builds_api import BuildsApi
from deadlock-api-client.api.commands_api import CommandsApi
from deadlock-api-client.api.custom_matches_api import CustomMatchesApi
from deadlock-api-client.api.e_sports_api import ESportsApi
from deadlock-api-client.api.info_api import InfoApi
from deadlock-api-client.api.internal_api import InternalApi
from deadlock-api-client.api.leaderboard_api import LeaderboardApi
from deadlock-api-client.api.mmr_api import MMRApi
from deadlock-api-client.api.matches_api import MatchesApi
from deadlock-api-client.api.patches_api import PatchesApi
from deadlock-api-client.api.players_api import PlayersApi
from deadlock-api-client.api.sql_api import SQLApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
