'use client';
import React, { useState } from 'react';

export default function Register() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Basic validation
    if (!firstName || !lastName || !email || !password || !confirmPassword) {
      setError('Please fill in all fields');
      return;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    // Simulating a registration request
    alert('Registration successful');
    setError('');
  };

  return (
    <div className="min-h-screen bg-gray-900 dark:bg-darkBackground text-white dark:text-darkText">

   

      {/* Registration Form Section */}
      <section className="py-20 flex justify-center items-center bg-gray-800">
        <div className="bg-gray-700 p-8 rounded-lg shadow-2xl w-full max-w-3xl">
          <h2 className="text-3xl font-bold text-center mb-6 text-gray-100">Register</h2>
          <form onSubmit={handleSubmit}>
            <div className="flex space-x-4 mb-6">
              <div className="flex-1">
                <label className="block text-sm font-semibold text-gray-300">First Name</label>
                <input
                  type="text"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  className="mt-1 p-3 w-full border border-gray-500 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700 dark:bg-gray-600 dark:text-gray-100"
                  placeholder="Enter your first name"
                />
              </div>
              <div className="flex-1">
                <label className="block text-sm font-semibold text-gray-300">Last Name</label>
                <input
                  type="text"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  className="mt-1 p-3 w-full border border-gray-500 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700 dark:bg-gray-600 dark:text-gray-100"
                  placeholder="Enter your last name"
                />
              </div>
            </div>

            <div className="mb-6">
              <label className="block text-sm font-semibold text-gray-300">Email</label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="mt-1 p-3 w-full border border-gray-500 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700 dark:bg-gray-600 dark:text-gray-100"
                placeholder="Enter your email"
              />
            </div>

            <div className="mb-6">
              <label className="block text-sm font-semibold text-gray-300">Password</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mt-1 p-3 w-full border border-gray-500 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700 dark:bg-gray-600 dark:text-gray-100"
                placeholder="Enter your password"
              />
            </div>

            <div className="mb-8">
              <label className="block text-sm font-semibold text-gray-300">Confirm Password</label>
              <input
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="mt-1 p-3 w-full border border-gray-500 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700 dark:bg-gray-600 dark:text-gray-100"
                placeholder="Confirm your password"
              />
            </div>

            {error && <p className="text-red-500 text-sm text-center mb-4">{error}</p>}
            <button
              type="submit"
              className="w-full py-3 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Register
            </button>
          </form>
        </div>
      </section>

      {/* Footer Section */}
      <footer className="bg-blue-900 text-white py-6">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <p className="mb-4 text-gray-400">© 2025 MedAI. All rights reserved.</p>
          <div className="flex justify-center space-x-6">
            <a href="https://facebook.com" className="hover:text-blue-300 transition duration-300">Facebook</a>
            <a href="https://twitter.com" className="hover:text-blue-300 transition duration-300">Twitter</a>
            <a href="https://linkedin.com" className="hover:text-blue-300 transition duration-300">LinkedIn</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
