<script lang="ts">
    type Team = {
        id: string;
        position: number;
        teamName: string;
        played: number;
        wins: number;
        draws: number;
        losses: number;
        goalsScored: number;
        goalsConceded: number;
        goalDiff: number;
        points: number;
    };

    let { id, name, teams }: { id: string; name: string; teams: Team[] } = $props();
</script>

<style>
    .group-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 0rem 1rem 1rem 1rem;
        width: 90%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .group-header {
        margin-bottom: 1rem;
        text-align: center;
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    td {
        padding: 0.5rem;
        text-align: left;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }
</style>

<div class="group-card">
    <div class="group-content">
        <div class="group-header">
            <h2>{name}</h2>
        </div>
        <table>
            <tbody>
                {#each teams as team(team.id)}
                    <tr>
                        <td>{team.position}</td>
                        <td>{team.teamName}</td>
                        <td>{team.played}</td>
                        <td>{team.points}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>