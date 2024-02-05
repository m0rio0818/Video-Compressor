import { InitialView } from "../view/initailView.js";

export class Controller {
    static renderInitialPage() {
        InitialView.create();
        let filepath : string = "";        
        let videoSelect = document.getElementById("video_select") as HTMLInputElement;
        videoSelect?.addEventListener("change", () => {
            let files = videoSelect?.files ?? [];
            if (files) {
                filepath = files[0].path;
                let textArea = document.getElementById("selected_video")
                textArea!.innerHTML = files[0].name;
                console.log("File path:", filepath); // ここでファイルのパスを取得
            } else {
                console.log("No file selected.");
            }
        })

        let conversionSelect = document.getElementById("conversion") as HTMLInputElement;
        conversionSelect.addEventListener("change", () =>{
            console.log("CHANGED!!")
            console.log(conversionSelect.value);
        })


    }
}
