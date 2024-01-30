export class InitialView{
    static create(){
        let root = document.getElementById("app")
        root!.innerHTML = "<h1>Hello World</h1>"

        console.log("HELLO!")
    }
}