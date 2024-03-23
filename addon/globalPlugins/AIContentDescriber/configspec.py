# Configuration specification for the AI Content Describer NVDA add-on
# Copyright (C) 2023, Carter Temm
# This add-on is free software, licensed under the terms of the GNU General Public License (version 2).
# For more details see: https://www.gnu.org/licenses/gpl-2.0.html


from io import StringIO


configspec = StringIO("""[GPT-4 vision]
api_key = string(default="")
prompt = string(default="Describe this image succinctly, but in as much detail as possible.")
max_tokens = integer(default=250)
cache_descriptions = boolean(default=False)
timeout = integer(default=10, min=1)
# these values are only maintained for backward compatibility and in case a downgrade is necessary
# changing them will do nothing on versions later than 2024.x.x.
# For that, please see the same options under the [global] section.
optimize_for_size = boolean(default=False)
open_in_dialog = boolean(default=False)

[Google Gemini pro vision]
api_key = string(default="")
prompt = string(default="Describe this image succinctly, but in as much detail as possible.")
max_tokens = integer(default=250)
cache_descriptions = boolean(default=False)
timeout = integer(default=10, min=1)

[global]
optimize_for_size = boolean(default=False)
open_in_dialog = boolean(default=False)
last_used_model = string(default="GPT-4 vision")
""")
