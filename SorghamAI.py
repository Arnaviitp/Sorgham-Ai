<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sorghum Disease Detector - AI Project</title>
    <!-- Tailwind CSS for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        body { font-family: 'Poppins', sans-serif; }
        .glass-effect {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
        }
        .animate-pulse-slow {
            animation: pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
    </style>
</head>
<body class="bg-gradient-to-br from-green-50 to-emerald-100 min-h-screen text-gray-800">

    <!-- Navigation -->
    <nav class="bg-emerald-800 text-white shadow-lg sticky top-0 z-50">
        <div class="container mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-2">
                <i class="fa-solid fa-leaf text-2xl text-green-300"></i>
                <span class="text-xl font-bold">SorghumAI</span>
            </div>
            <div class="hidden md:flex space-x-8 text-sm font-semibold">
                <a href="#home" class="hover:text-green-300 transition">Home</a>
                <a href="#upload" class="hover:text-green-300 transition">Detect Disease</a>
                <a href="#tech" class="hover:text-green-300 transition">Tech Stack</a>
                <a href="#team" class="hover:text-green-300 transition">Team</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="container mx-auto px-6 py-16 flex flex-col md:flex-row items-center">
        <div class="md:w-1/2 mb-10 md:mb-0">
            <span class="bg-green-100 text-emerald-800 px-3 py-1 rounded-full text-xs font-bold tracking-wide uppercase">Major Project 2026</span>
            <h1 class="text-4xl md:text-5xl font-bold leading-tight mt-4 mb-6 text-emerald-900">
                Protecting Crops with <br> <span class="text-green-600">Artificial Intelligence</span>
            </h1>
            <p class="text-lg text-gray-600 mb-8 leading-relaxed">
                Early detection of Sorghum crop diseases using Convolutional Neural Networks (CNN). 
                Upload a leaf image and get instant analysis.
            </p>
            <a href="#upload" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition transform hover:-translate-y-1">
                Try Live Demo <i class="fa-solid fa-arrow-right ml-2"></i>
            </a>
        </div>
        <div class="md:w-1/2 flex justify-center relative">
            <div class="absolute inset-0 bg-green-200 rounded-full filter blur-3xl opacity-30 animate-pulse-slow"></div>
            <!-- Using an icon representation for the demo -->
            <div class="bg-white p-8 rounded-2xl shadow-2xl z-10 text-center w-80">
                <i class="fa-solid fa-shield-virus text-6xl text-emerald-500 mb-4"></i>
                <div class="h-2 bg-gray-200 rounded mt-2 mb-2 w-full"><div class="h-full bg-emerald-500 rounded w-3/4"></div></div>
                <p class="text-xs text-gray-400">Analysis in progress...</p>
                <div class="mt-4 flex justify-between text-sm font-bold text-gray-700">
                    <span>Accuracy</span>
                    <span>98.5%</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Upload/Demo Section -->
    <section id="upload" class="bg-white py-20 shadow-inner">
        <div class="container mx-auto px-6 text-center">
            <h2 class="text-3xl font-bold text-emerald-900 mb-4">Disease Detection Demo</h2>
            <p class="text-gray-500 mb-10 max-w-2xl mx-auto">Upload an image of a Sorghum leaf to simulate our Deep Learning model's prediction process.</p>

            <div class="max-w-xl mx-auto bg-gray-50 border-2 border-dashed border-emerald-300 rounded-xl p-10 hover:bg-green-50 transition cursor-pointer relative" id="drop-zone">
                <input type="file" id="file-input" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer" accept="image/*">
                
                <div id="upload-content">
                    <i class="fa-solid fa-cloud-arrow-up text-5xl text-emerald-400 mb-4"></i>
                    <h3 class="text-xl font-semibold text-gray-700">Click to Upload Image</h3>
                    <p class="text-sm text-gray-500 mt-2">Supports JPG, PNG (Max 5MB)</p>
                </div>

                <!-- Hidden Loading State -->
                <div id="loading-state" class="hidden">
                    <i class="fa-solid fa-circle-notch fa-spin text-5xl text-emerald-600 mb-4"></i>
                    <h3 class="text-xl font-semibold text-gray-700">Analyzing Leaf Patterns...</h3>
                    <p class="text-sm text-gray-500 mt-2">Running CNN Model</p>
                </div>
            </div>

            <!-- Result Card (Hidden by default) -->
            <div id="result-card" class="hidden max-w-xl mx-auto mt-8 bg-white border border-gray-200 rounded-xl shadow-xl overflow-hidden text-left transform transition-all duration-500 scale-95 opacity-0">
                <div class="bg-emerald-600 p-4 flex justify-between items-center">
                    <h3 class="text-white font-bold text-lg"><i class="fa-solid fa-check-circle mr-2"></i> Analysis Complete</h3>
                    <button onclick="resetDemo()" class="text-emerald-100 hover:text-white text-sm underline">Reset</button>
                </div>
                <div class="p-6">
                    <div class="flex items-start space-x-4">
                        <div class="bg-red-100 p-3 rounded-lg">
                            <i class="fa-solid fa-triangle-exclamation text-red-500 text-2xl"></i>
                        </div>
                        <div class="flex-1">
                            <p class="text-xs text-gray-500 uppercase font-bold tracking-wider">Detected Disease</p>
                            <h2 class="text-2xl font-bold text-gray-800" id="disease-name">Anthracnose</h2>
                            <p class="text-sm text-gray-600 mt-1">A fungal disease causing small red spots on leaves.</p>
                        </div>
                        <div class="text-right">
                            <p class="text-xs text-gray-500 uppercase font-bold tracking-wider">Confidence</p>
                            <span class="text-2xl font-bold text-emerald-600">96.4%</span>
                        </div>
                    </div>
                    
                    <div class="mt-6 pt-6 border-t border-gray-100">
                        <h4 class="text-sm font-bold text-gray-700 mb-2">Recommended Action:</h4>
                        <ul class="text-sm text-gray-600 space-y-2">
                            <li><i class="fa-solid fa-arrow-right text-emerald-500 mr-2"></i>Apply fungicides containing Azoxystrobin.</li>
                            <li><i class="fa-solid fa-arrow-right text-emerald-500 mr-2"></i>Rotate crops to reduce fungal spores in soil.</li>
                        </ul>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Tech Stack Section -->
    <section id="tech" class="container mx-auto px-6 py-20">
        <h2 class="text-3xl font-bold text-emerald-900 mb-12 text-center">Technology Stack</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            
            <div class="p-6 bg-white rounded-xl shadow-md hover:shadow-lg transition">
                <i class="fa-brands fa-python text-5xl text-blue-500 mb-4"></i>
                <h3 class="font-bold text-gray-800">Python</h3>
                <p class="text-xs text-gray-500 mt-1">Core Logic</p>
            </div>

            <div class="p-6 bg-white rounded-xl shadow-md hover:shadow-lg transition">
                <i class="fa-solid fa-brain text-5xl text-orange-500 mb-4"></i>
                <h3 class="font-bold text-gray-800">TensorFlow</h3>
                <p class="text-xs text-gray-500 mt-1">Deep Learning</p>
            </div>

            <div class="p-6 bg-white rounded-xl shadow-md hover:shadow-lg transition">
                <i class="fa-solid fa-database text-5xl text-yellow-500 mb-4"></i>
                <h3 class="font-bold text-gray-800">Pandas</h3>
                <p class="text-xs text-gray-500 mt-1">Data Processing</p>
            </div>

            <div class="p-6 bg-white rounded-xl shadow-md hover:shadow-lg transition">
                <i class="fa-brands fa-html5 text-5xl text-orange-600 mb-4"></i>
                <h3 class="font-bold text-gray-800">HTML/Tailwind</h3>
                <p class="text-xs text-gray-500 mt-1">Frontend Interface</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-emerald-900 text-emerald-200 py-8 text-center">
        <p>&copy; 2026 Team. Major Project.</p>
    </footer>

    <!-- Script for Simulation Logic -->
    <script>
        const fileInput = document.getElementById('file-input');
        const uploadContent = document.getElementById('upload-content');
        const loadingState = document.getElementById('loading-state');
        const resultCard = document.getElementById('result-card');
        const diseaseName = document.getElementById('disease-name');

        // Random mock results for the demo
        const mockDiseases = [
            "Anthracnose",
            "Leaf Blight",
            "Rust",
            "Downy Mildew"
        ];

        fileInput.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                // 1. Hide upload content, show loading
                uploadContent.classList.add('hidden');
                loadingState.classList.remove('hidden');

                // 2. Simulate processing delay (2 seconds)
                setTimeout(() => {
                    loadingState.classList.add('hidden');
                    
                    // 3. Pick a random disease for demo purposes
                    const randomDisease = mockDiseases[Math.floor(Math.random() * mockDiseases.length)];
                    diseaseName.innerText = randomDisease;

                    // 4. Show result card with animation
                    resultCard.classList.remove('hidden');
                    // Small delay to allow 'display: block' to apply before opacity transition
                    setTimeout(() => {
                        resultCard.classList.remove('scale-95', 'opacity-0');
                        resultCard.classList.add('scale-100', 'opacity-100');
                    }, 50);

                }, 2000);
            }
        });

        function resetDemo() {
            // Reset UI
            resultCard.classList.add('scale-95', 'opacity-0');
            setTimeout(() => {
                resultCard.classList.add('hidden');
                uploadContent.classList.remove('hidden');
                fileInput.value = ""; // Clear input
            }, 500);
        }
    </script>
</body>
</html>
