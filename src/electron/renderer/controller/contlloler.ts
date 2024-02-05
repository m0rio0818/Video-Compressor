import { InitialView } from "../view/initailView.js";
import { selectView } from "../view/selectView.js";

export class Controller {
    static renderInitialPage() {
        InitialView.create();
        let filepath: string = "";
        let videoSelect = document.getElementById(
            "video_select"
        ) as HTMLInputElement;
        videoSelect?.addEventListener("change", () => {
            let files = videoSelect?.files ?? [];
            if (files) {
                filepath = files[0].path;
                let textArea = document.getElementById("selected_video");
                textArea!.innerHTML = files[0].name;
                console.log("File path:", filepath); // ここでファイルのパスを取得
            } else {
                console.log("No file selected.");
            }
        });

        let conversionSelect = document.getElementById(
            "conversion"
        ) as HTMLInputElement;
        conversionSelect.addEventListener("change", () => {
            let typeOfConvresion = conversionSelect.value;
            console.log(typeOfConvresion);

            if (typeOfConvresion == "compression") {
                selectView.clearArea();
                selectView.compressoinView();
            } else if (typeOfConvresion == "resolution") {
                selectView.clearArea();
                selectView.resolutionView();
            } else if (typeOfConvresion == "aspect") {
                selectView.clearArea();
                selectView.aspectView();
            } else if (typeOfConvresion == "mp3") {
                selectView.clearArea();
                selectView.mp3View();
            } else if (typeOfConvresion == "gif") {
                selectView.clearArea();
                selectView.gifView();
            } else if (typeOfConvresion == "webm") {
                selectView.clearArea();
                selectView.webmView();
            } else {
            }
        });

        let convertButton = document.getElementById(
            "conversion"
        ) as HTMLInputElement;

        convertButton.addEventListener("click", () => {});
    }
}
