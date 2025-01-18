// src/app/layout.js
import './globals.css'; // Import global styles (for dark mode or other global styles)

export default function Layout({ children }) {
  return (
    <html lang="en">
      <body className="bg-white text-black dark:bg-darkBackground dark:text-darkText">
        <header className="bg-gradient-to-r from-purple-600 via-pink-500 to-purple-600 text-white py-6 shadow-md">
          <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
            <h1 className="text-4xl font-bold font-serif">MedAI</h1>
            <nav>
              <ul className="flex space-x-6">
                <li><a href="/" className="hover:text-gray-300">Home</a></li>
                <li><a href="/#features" className="hover:text-gray-300">Features</a></li>
                <li><a href="/#about" className="hover:text-gray-300">About</a></li>
                <li><a href="/#contact" className="hover:text-gray-300">Contact</a></li>
                <li><a href="/login" className="hover:text-gray-300">Login</a></li>
              </ul>
            </nav>
          </div>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
