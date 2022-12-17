import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignUpView from '../views/SignUpView.vue'
import CreateReviewView from '../views/CreateReviewView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/search',
    name: 'Search',
    component: HomeView
  },
  {
    path: '/',
    name: 'home',
    component: MovieListView,
  },
  {
    path: '/movielist/:id',
    name: 'MovieDetail',
    component: MovieDetailView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView,
  },
  {
    path: '/movielist/reviews/:id',
    name: 'CreateReview',
    component: CreateReviewView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
