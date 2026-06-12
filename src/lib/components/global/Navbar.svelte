<script lang="ts">
    import { page } from '$app/state';
    import navlogo from '$lib/assets/logos/wc26_black.png';
</script>
<style>
    .navbar {
        background-color: #ffffff;
        padding: 0.8rem 2.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .navbar-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .nav-logo-image {
        height: 50px;
    }

    .nav-links {
        list-style: none;
        display: flex;
        gap: 1.5rem;
        margin: 0;
        padding: 0;
    }

    .nav-link {
        text-decoration: none;
        color: #333333;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        position: relative;
    }

    .nav-link:hover {
        color: #ff710a;
    }

    .nav-link.active::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -5px;
        width: 100%;
        height: 2px;
        background-color: #ff710a;
    }
</style>
<nav class="navbar">
    <div class="navbar-container">
        <a href="/" class="nav-logo">
            <img src={navlogo} alt="WC26 Black Logo" class="nav-logo-image" />
        </a>
        <ul class="nav-links">
            <li class="nav-item">
                <a href="/schedule" class="nav-link" class:active={page.url.pathname.startsWith('/schedule')}>
                    Schedule
                </a>
            </li>
            <li class="nav-item">
                <a href="/preview" class="nav-link" class:active={page.url.pathname.startsWith('/preview')}>
                    Preview
                </a>
            </li>
            <li class="nav-item">
                <a href="/live" class="nav-link" class:active={page.url.pathname.startsWith('/live')}>
                    Live
                </a>
            </li>
        </ul>
    </div>
</nav>