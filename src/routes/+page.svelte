<script>
    import wclogo from '$lib/assets/logos/wc26_white.png';
</script>
<style>
    /* Global styles */
    :global(html, body) {
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
    }

    :global(h1, p) {
        margin-top: 0;
    }

    /* Home page styles */
    .home-hero-container {
        background-image: url('$lib/assets/img/hero_bg.png');
        background-size: cover;
        background-position: center;
        min-height: 100vh;
        max-height: 100vh;
    }

    .home-content {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        text-align: left;
        color: white;
    }

    .home-hero {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .home-hero-title > p {
        font-size: 4rem;
        margin-bottom: 0.1rem;
        letter-spacing: -2%;
    }

    /* Button styles */
    .home-hero-btn {
        display: flex;
        gap: 1rem;
    }

    .home-hero-btn button {
        padding: 0.7rem 0.9rem;
        font-size: 1rem;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-weight: 450;
    }

    .home-hero-btn button:hover {
        background-color: rgb(255, 113, 10);
        transition: background-color 0.3s ease;
    }

    .home-hero-btn button a {
        color: black;
        text-decoration: none;
    }

    /* Info button styles */
    .home-info-btn {
        position: absolute;
        background: none;
        border: none;
        color: white;
        cursor: pointer;
        top: 0.5rem;
        right: 0.5rem;
        line-height: 0;
    }
</style>
<div class="home-hero-container">
    <div class="home-info-btn">
        <button class="home-info-btn">
            <span class="material-symbols-outlined">
                info
            </span>
        </button>
    </div>
    <div class="home-content">
        <img src={wclogo} alt="World Cup Logo" width="250" />
        <div class="home-hero">
            <div class="home-hero-title">
                <p><b>World Cup</b></p>
                <p><b>Anything & Everything</b></p>
            </div>
            <div class="home-hero-btn">
                <button class="schedule-btn">
                    <a href="/schedule">Schedule</a>
                </button>
                <button class="preview-btn">
                    <a href="/preview">Preview</a>
                </button>
                <button class="live-btn">
                    <a href="/live">Live</a>
                </button>
            </div>
        </div>
    </div>
</div>
