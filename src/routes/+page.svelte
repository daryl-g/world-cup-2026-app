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
        font-family: 'Inter', sans-serif;
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

    .info-popup {
        display: none;
        position: absolute;
        top: 2.5rem;
        right: 0.5rem;
        align-items: center;
        justify-content: center;
        background-color: rgba(0, 0, 0, 0.8);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        color: white;
        padding: 1.5rem 0.8rem 0.5rem;
        border-radius: 10px;
        width: max-content;
    }

    .home-info-btn:hover + .info-popup {
        display: block;
    }
</style>
<div class="home-hero-container">
    <div class="home-info-btn">
        <button class="home-info-btn" aria-label="Info">
            <span class="material-symbols-outlined">
                info
            </span>
        </button>
        <div class="info-popup">
            <p>Made with ❤️ by Daryl</p>
            <br />
            <p>https://daryldao.com</p>
        </div>
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
