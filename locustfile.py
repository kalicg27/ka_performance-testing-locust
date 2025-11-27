from tests.user_scenarios import ReadOnlyUser, WriteHeavyUser
from tests.utils import TARGET_HOST

ReadOnlyUser.host = TARGET_HOST
WriteHeavyUser.host = TARGET_HOST
