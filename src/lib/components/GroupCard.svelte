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

    let {
        id,
        name,
        primaryColor,
        textColor,
        teams
    }: {
        id: string;
        name: string;
        primaryColor: string;
        textColor: string;
        teams: Team[];
    } = $props();
</script>

<style>
    .group-card {
        background: rgba(255, 255, 255, 0.3);
        color: black;
        border-radius: 10px;
        width: 90%;
        height: fit-content;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .group-header {
        width: 100%;
        height: fit-content;
        border-radius: 10px 10px 0 0;
        text-align: center;
        font-weight: bold;
        font-size: 1.3rem;
    }

    .group-detailed {
        text-decoration: none;
        cursor: pointer;
    }

    .group-header p {
        padding: 0.5rem 0 0.5rem 0;
    }

    .group-teams {
        padding: 0 0.3rem;
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
        <a class="group-detailed" href="/schedule/{id}">
            <div class="group-header" style="background-color: {primaryColor}; color: {textColor};"> 
                <p>{name}</p> 
            </div>
        </a>
        <div class="group-teams">
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
</div>