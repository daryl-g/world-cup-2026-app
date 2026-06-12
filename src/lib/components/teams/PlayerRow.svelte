<script lang="ts">
    // Static type
    type Player = {
        id: string;
        shirtNumber: number;
        playerName: string;
        position: string;
        parentClub: string;
    };

    // Data
    let { player, shirt }: { player: Player; shirt: string } = $props();
</script>

<style>
    .player-row {
        display: grid;
        grid-template-columns: 0.1fr 0.1fr 1fr 1fr;
        gap: 1rem;
        align-items: center;
        padding: 0.5rem;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }

    .player-shirt {
        position: relative;
        display: flex;
        align-items: center;
        width: fit-content;
    }

    .player-shirt p {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -40%);
        margin: 0;
        font-weight: 700;
        font-size: 0.95rem;
    }

    .player-name {
        font-size: 1.1rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
    }

    .player-club {
        justify-self: end;
        padding-right: 1rem;
    }
</style>

<div class="player-row">
    <div class="player-shirt">
        <img src={shirt} alt="Team shirt" width=40 />
        <p>{player.shirtNumber}</p>
    </div>
    <div class="player-position">
        <p>{player.position}</p>
    </div>
    <div class="player-name">
        <p>{player.playerName}</p>
    </div>
    <div class="player-club">
        <p>{player.parentClub}</p>
    </div>
</div>