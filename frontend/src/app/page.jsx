// src/app/page.js
import Image from "next/image";

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-b from-black to-pink-900 text-white dark:text-darkText">
      {/* Hero Section: 50vh */}
      <section className="flex flex-row justify-between items-center bg-gray-800 h-[86vh] relative">
        
        {/* Left Section: Text and Button */}
        <div className="flex-1 flex flex-col justify-center items-center px-8">
          <div className="text-center">
            <h2 className="text-5xl font-extrabold mb-6 text-gray-100 font-serif">Welcome to MedAI</h2>
            <p className="text-xl mb-8 text-gray-300 animate-typing font-dancing-script">
              Your personal, around-the-clock AI Doctor
            </p>
            <div>
            <a 
              href="/register" 
              className="bg-pink-500 text-white px-8 py-4 rounded-lg text-xl hover:bg-pink-600 transition duration-300 transform hover:scale-105 shadow-md">
              Sign up now!
            </a>
            </div>
            
          </div>
        </div>

        {/* Right Section: Image */}
        <div className="flex-1 flex justify-center items-center pr-8">
          <div className="relative flex justify-center items-center">
            <Image src="/[CITYPNG.COM]Transparent HD Caduceus White Medical Symbol Silhouette - 1500x1500.png" width={400} height={400} alt="Ambulance Icon" />
          </div>
        </div>
      </section>

      {/* Features Section: 50vh */}
      <section id="features" className="flex flex-col h-[86vh] justify-center items-center bg-gradient-to-b from-gray-800 via-pink-800 to-pink-900">
        <div className="max-w-7xl mx-auto text-center px-6 flex flex-col justify-center items-center w-full">
          <h2 className="text-4xl text-gray-100 font-bold mb-12">Our Features</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-12 w-full">
            <div className="bg-gray-700 shadow-2xl rounded-lg px-3 py-8 transition-transform transform hover:scale-105">
              <h3 className="text-2xl font-semibold mb-4 text-white">AI-Powered Symptom Diagnoses</h3>
              <p className="text-gray-300">Our AI provides fast and insightful awareness and identification of illness, improving your healthcare experience.</p>
            </div>
            <div className="bg-gray-700 shadow-2xl rounded-lg px-3 py-8 transition-transform transform hover:scale-105">
              <h3 className="text-2xl font-semibold mb-4 text-white">Comprehensive Symptom Checker</h3>
              <p className="text-gray-300">Leverage our vast medical database for accurate and efficient diagnoses, helping you get the right care.</p>
            </div>
            <div className="bg-gray-700 shadow-2xl rounded-lg px-3 py-8 transition-transform transform hover:scale-105">
              <h3 className="text-2xl font-semibold mb-4 text-white">24/7 Availability</h3>
              <p className="text-gray-300">Our AI doctor is always available, providing support whenever you need it, day or night.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="bg-pink-900 text-white py-6">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <p className="mb-4 text-gray-400">© 2025 MedAI. All rights reserved.</p>
          <div className="flex justify-center space-x-6">
            <a href="https://facebook.com" className="hover:text-pink-300 transition duration-300">Facebook</a>
            <a href="https://twitter.com" className="hover:text-pink-300 transition duration-300">Twitter</a>
            <a href="https://linkedin.com" className="hover:text-pink-300 transition duration-300">LinkedIn</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
