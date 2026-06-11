<script lang="ts">
    let { id, name, teams }: { id: string; name: string; teams: string[] } = { id: '', name: '', teams: [] };
</script>

<style></style>

<div class="group-card">
    <h3>{name}</h3>
    <ul>
        {#each teams as team}
            <li>{team}</li>
        {/each}
    </ul>
</div>