class topBar extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      this.render();
    }
  
    render() {
      this.innerHTML = `
        <nav class="w-full h-1/4 py-12 bg-blue-800 shadow flex-none">
            <div class="w-full container mx-auto flex flex-wrap items-center justify-between">

                <nav>
                    <ul class="flex items-center justify-between font-bold text-sm text-white uppercase no-underline">
                        <li><a class="hover:text-gray-200 hover:underline px-4" href="#">Temperature - 28°C</a></li>
                        <li><a class="hover:text-gray-200 hover:underline px-4" href="#">Humidity - 75%</a></li>
                    </ul>
                </nav>

                <div class="flex items-center justify-between text-sm uppercase no-underline text-white pr-6">
                <a class="hover:text-gray-200 hover:underline px-4" href="#">23/8/2021</a>
                <a class="hover:text-gray-200 hover:underline px-4" href="#">2:22am</a>

                </div>
            </div>

        </nav>
        `;
    }
  }
  
  customElements.define("top-bar", topBar);