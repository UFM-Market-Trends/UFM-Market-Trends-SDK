# This is so that we can write
# `import ufmtrends_sdk` or `import test from ufmtrends_sdk`
# instead of 
# `from ufmtrends_sdk.functions import test`

from .functions import test, get_yearly_values, get_yearly_variation
from .functions import get_yearonyear_variation
from .functions import get_accumulated_values, get_accumulated_variation