const STANDING_URL =
  "https://raw.githubusercontent.com/daryl-g/world-cup-2026-app/refs/heads/main/data/standings.json";

export async function load() {
  const response = await fetch(STANDING_URL);
  const standings: Record<string, any> = await response.json();

  return standings;
}
