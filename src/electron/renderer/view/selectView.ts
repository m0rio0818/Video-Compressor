export class selectView {
    static clearArea() {
        let option = document.getElementById("optionArea")!;
        console.log(option);
        if (option) {
            option.innerHTML = ``;
        }
    }

    static clearCustomArea(){
        let custom_area = document.getElementById("custom_input_area");
        custom_area!.innerHTML = "";
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
    }

    static resolutionView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `
        <div class="max-w-md mx-auto p-8">
            <label for="resolution" class="cursor-pointer text-center">解像度選択: </label>
            <div class="relative inline-block mx-auto text-center">
                <select id="resolution" class="px-4 py-2 focus:outline-none">
                    <option disabled selected>選択してください</option>
                    <option value="720p">720p</option>
                    <option value="1080p">1080p</option>
                    <option value="wqhd">WQHD</option>
                    <option value="4k">4K</option>
                    <option value="8k">8K</option>
                    <option value="custom">カスタム</option>
                </select>
            </div>
            <div id="custom_input_area"></div>
        </div>

        `;
    }

    static customInput() {
        let custom_area = document.getElementById("custom_input_area");
        let customInput = `
        <div>
            <div>
                <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>
                <input type="text" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required>
            </div>
            <div>
                <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>
                <input type="text" id="last_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required>
            </div>
        </div>
        `;
        custom_area!.innerHTML = customInput;
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
