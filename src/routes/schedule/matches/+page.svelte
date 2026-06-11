<script lang="ts">
    // Static types
    type Sort = 'date' | 'group' | 'round';
    let activeSort: Sort = $state<Sort>('date');
</script>

<style>
    .matches-content {
        background: rgba(255, 255, 255, 0.5);
        border-radius: 0px 0px 10px 10px;
        width: 100%;
        height: 100%;
    }

    .matches-sort {
        display: flex;
        align-items: center;
        justify-content: center;
        color: black;
        gap: 0.5rem;
        padding: 1rem;
    }

    .matches-sort button {
        background: rgba(255, 255, 255);
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        color: black;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s;
    }
</style>

<div class="matches-content">
    <div class="matches-sort">
        <h3>Sort by:</h3>
        <button onclick={() => activeSort = 'date'} class:active={activeSort === 'date'}>Date</button>
        <button onclick={() => activeSort = 'group'} class:active={activeSort === 'group'}>Group</button>
        <button onclick={() => activeSort = 'round'} class:active={activeSort === 'round'}>Round</button>
    </div>
</div>