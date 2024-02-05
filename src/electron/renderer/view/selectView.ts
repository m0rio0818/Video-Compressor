export class selectView{
     static clearArea() {
        let option = document.getElementById("optionArea")!;
        console.log(option);
        if (option){
            option.innerHTML = ``;
        }
    }

    static compressoinView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `
        <div class="max-w-md mx-auto p-8">
            <h2 class="text-2xl font-bold mb-4 text-center">圧縮レベル</h2>
        
            <label class="flex items-center space-x-2">
              <input type="radio" name="radioOption" class="text-sky-500 form-radio focus:ring-sky-500 h-4 w-4">
              <span class="text-gray-800">High</span>
            </label>
        
            <label class="flex items-center space-x-2">
              <input type="radio" name="radioOption" class="text-sky-500 form-radio focus:ring-sky-500 h-4 w-4">
              <span class="text-gray-800">Normal</span>
            </label>
        
            <label class="flex items-center space-x-2">
              <input type="radio" name="radioOption" class="text-sky-500 form-radio focus:ring-sky-500 h-4 w-4">
              <span class="text-gray-800">Low</span>
            </label>
        </div>
        `;

        console.log(option.innerHTML);
    }

    static resolutionView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

        `;
    }

    static aspectView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }

    static mp3View() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }

    static gifView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }
    static webmView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }
}
