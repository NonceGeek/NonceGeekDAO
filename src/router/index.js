import Home from '../pages/Home.vue';
import Series from '../pages/Series.vue';
import Camp from '../pages/Camp.vue';
import Builders from '../pages/Builders.vue';
import Artist from '../pages/Artist.vue';
import Partners from '../pages/Partners.vue';
import About from '../pages/About.vue';
import WhitePaper from '../pages/WhitePaper.vue';
import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/whitepaper', name: 'whitepaper', component: WhitePaper },
    { path: '/series', name: 'series', component: Series },
    { path: '/camp', name: 'camp', component: Camp },
    { path: '/builders', name: 'builders', component: Builders },
    { path: '/artist', name: 'artist', component: Artist },
    { path: '/partners', name: 'partners', component: Partners },
    { path: '/about', name: 'about', component: About },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router;