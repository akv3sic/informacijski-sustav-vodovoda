import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

/********************************************/
/**************** ROUTES ********************/
/********************************************/

const routes = [
  // home
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Informacijski sustav vodovoda',
      metaTags: [
        {
          name: 'description',
          content: 'Sustav za upravljanje poslovanjem vodovoda.'
        },
        {
          property: 'og:description',
          content: 'Sustav za upravljanje poslovanjem vodovoda..'
        }
      ]
    }
  },
  // FAQs
  {
    path: '/cesto-postavljana-pitanja',
    name: "FAQs",
    component: () => import("@/views/FAQs")
  },
  // sve novosti
  {
    path: '/novosti',
    name: "posts",
    component: () => import("@/views/posts/AllPosts"),
  },
  //pojedinačna novost (objava)
  {
    path: '/novosti/:id/:slug',
    name: "post",
    component: () => import("@/views/posts/Post"),
    props: true
  },
  // auth
  {
    path: '/registracija',
    name: 'registracija',
    component: () => import("@/views/auth/Register")
  },
  {
    path: '/prijava',
    name: 'login',
    component: () => import("@/views/auth/Login")
  },
  {
    path: '/resetiranje-lozinke',
    name: 'reset-password',
    component: () => import("@/views/auth/ResetPassword")
  },

  /************************************/
  /********* administracija ***********/
  /************************************/
  {
    path: '/admin',
    component: () => import("@/views/admin/AdminHome"),
    meta: {  },
    children: [

    ]
  },
  /************************************/
  /************************************/
  /************************************/
  /********* popisivanje ***********/
  /************************************/
  {
    path: '/popisivaci',
    redirect: '/popisivaci/pregled-prikljucaka',
    component: () => import("@/views/staff/Home"),
    meta: {  },
    children: [
      {
        path: 'pregled-prikljucaka',
        name: 'contracts-staff',
        component: () => import("@/views/staff/ContractsOverview"),
      },
    ]
  },
  /************************************/
  /************************************/
  /**************************************/
  /********* korisnički račun ***********/
  /**************************************/
  {
    path: '/moj-racun',
    redirect: '/moj-racun/osobni-podatci',
    component: () => import("@/views/userDashboard/Home"),
    meta: {  },
    children: [
      {
        path: 'osobni-podatci',
        name: 'account-details',
        component: () => import("@/views/userDashboard/AccountDetails"),
      },
      {
        path: 'racuni',
        name: 'user-bills',
        component: () => import("@/views/userDashboard/Bills"),
      },
      {
        path: 'pregled-potrosnje',
        name: 'user-consuption-overview',
        component: () => import("@/views/userDashboard/ConsumptionOverview"),
      },
      {
        path: 'prijava-kvara',
        name: 'user-malfunction-report',
        component: () => import("@/views/userDashboard/MalfunctionReport"),
      },
      {
        path: 'postavke',
        name: 'user-settings',
        component: () => import("@/views/userDashboard/Settings"),
      },
      {
        path: 'novi-prikljucak',
        name: 'user-new-contract',
        component: () => import("@/views/userDashboard/NewContract"),
      },
    ]
  },
  /************************************/
  /************************************/

  // 404 redirect - ovo TREBA stojati na kraju
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: () => import("@/views/NotFound"),
    meta: {
      title: 'Stranica nije pronađena',
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


/********************************************/
/************ NAVIGATION GUARDS *************/
/********************************************/

/*----------- SET META ------------*/

// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
  // `/nested`'s will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if(nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  } else if(previousNearestWithMeta) {
    document.title = previousNearestWithMeta.meta.title;
  }

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  // Skip rendering meta tags if there are none.
  if(!nearestWithMeta) return next();

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');

    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });

    // We use this to track which meta tags we create so we don't interfere with other ones.
    tag.setAttribute('data-vue-router-controlled', '');

    return tag;
  })
  // Add the meta tags to the document head.
  .forEach(tag => document.head.appendChild(tag));

  next();
});


export default router
