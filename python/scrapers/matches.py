# Scrape results and standings from Wikipedia and update the JSON files

# Imports
import os
import json
import requests
import pandas as pd

from loguru import logger
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ----------------------------------------------------------

# Load lookup tables
with open("data/groups.json", "r") as f:
    groups_data = json.load(f)
    f.close()

groups_lookup = pd.DataFrame(groups_data["groups"])
logger.success("Loaded groups lookup table")

with open("data/teams.json", "r") as f:
    teams_data = json.load(f)
    f.close()

teams_lookup = pd.DataFrame(teams_data["teams"])
logger.success("Loaded teams lookup table")

with open("data/stages.json", "r") as f:
    stages_data = json.load(f)
    f.close()

stages_lookup = pd.DataFrame(stages_data["stages"])
logger.success("Loaded stages lookup table")

# ----------------------------------------------------------
# Determine which stage of the tournament is currently happening
current_stage = stages_lookup[
    (stages_lookup["startDate"] <= datetime.now().strftime("%Y-%m-%d"))
    & (stages_lookup["endDate"] >= datetime.now().strftime("%Y-%m-%d"))
]["name"].values[0]

logger.info(f"Current stage of the 2026 World Cup: {current_stage}")

matches = []

# Check if the matches json file contains data or not
# Making sure that the IDs don't get rotated when the file is updated with new matches

# Scrape match info and data from Wikipedia based on current stage
if current_stage == "Group Stage":
    for group in groups_lookup["name"]:
        request = requests.get(
            f"https://en.wikipedia.org/api/rest_v1/page/html/2026_FIFA_World_Cup_{group.replace(' ', '_')}",
            headers={"User-Agent": f"World-Cup-2026-App/1.0 ({os.environ['EMAIL']})"},
        )

        soup = BeautifulSoup(request.text, "html.parser")
else:
    request = requests.get(
        "https://en.wikipedia.org/api/rest_v1/page/html/2026_FIFA_World_Cup_knockout_stage",
        headers={"User-Agent": f"World-Cup-2026-App/1.0 ({os.environ['EMAIL']})"},
    )

    soup = BeautifulSoup(request.text, "html.parser")
