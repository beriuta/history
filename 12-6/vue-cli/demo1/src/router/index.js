import VueRouter from 'vue-router'
import Dessert from '../components/header/dessert'
import Vue from 'vue'

Vue.use(VueRouter);

let url = [
  {
    path:'/',
    component: Dessert
  }
];

let router = new VueRouter({
    routes:url
});

export default router   // 抛出router


//实例化VueRouter和抛出还可以这么写
// export default new VueRouter({
//     routes:url
// });
