import Vue from "vue"
import Router from "vue-router"
import Page1 from "@/components/Page1";
import HelloWorld from "@/components/HelloWorld";

Vue.use(Router)

const router = new Router({
    routes: [
        {
            path: "/",
            name: "home",
            component: HelloWorld
        },
        {
            path: "/users",
            name: "users",
            component: Page1
        }
    ],
    mode: "history"
})

export default router
