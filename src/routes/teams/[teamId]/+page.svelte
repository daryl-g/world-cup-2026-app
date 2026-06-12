<script lang="ts">
    // Data
    let { data } = $props();
</script>

<style></style>

<div class="team-detailed-container">
    <div class="team-header" style="background-color: {data.team.primaryColor}; color: {data.team.textColor}">
        <img src={data.team.flag} alt="{data.team.shortName} flag" width=30 class="team-flag" />
        <h1>{data.team.fullName}</h1>
    </div>
    <div class="team-info">
        <div class="team-squad">
            <h2>Squad</h2>
            <ul>
                {#each data.team.squad as player}
                    <li>{player.name} - {player.position}</li>
                {/each}
            </ul>
        </div>
    </div>
</div>