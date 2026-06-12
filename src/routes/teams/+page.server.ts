const BASE_URL =
  "https://raw.githubusercontent.com/daryl-g/world-cup-2026-app/refs/heads/main/data";

export async function load() {
  const teamsResponse = await fetch(`${BASE_URL}/teams.json`);
  const teams = await teamsResponse.json();
  return teams;
}
