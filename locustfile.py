from locust import events
from tests.utils import TARGET_HOST, LOAD_PROFILE
from tests.user_scenarios import ReadOnlyUser, WriteHeavyUser


# Expose host on users
ReadOnlyUser.host = TARGET_HOST
WriteHeavyUser.host = TARGET_HOST


@events.init_command_line_parser.add_listener
def _(parser):
    """
    Extend Locust CLI with sensible defaults from YAML if not provided.
    This makes it easy to run locally and in CI.
    """
    parser.add_argument(
        "--users",
        type=int,
        env_var="LOCUST_USERS",
        default=LOAD_PROFILE["users"],
        help="Number of concurrent users (default from config/settings.yaml)."
    )
    parser.add_argument(
        "--spawn-rate",
        type=float,
        env_var="LOCUST_SPAWN_RATE",
        default=LOAD_PROFILE["spawn_rate"],
        help="Spawn rate users/sec (default from config/settings.yaml)."
    )
    parser.add_argument(
        "--run-time",
        type=str,
        env_var="LOCUST_RUN_TIME",
        default=LOAD_PROFILE["run_time"],
        help="Run time, e.g. 1m, 5m (default from config/settings.yaml)."
    )
