npx create-react-app my-portfolio
cd my-portfolio
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
[21:34, 01.02.2025] Александр(Сапфир): module.exports = {
  content: ["./src/*/.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
@tailwind base;
@tailwind components;
@tailwind utilities
import React from "react";
import Hero from "./components/Hero";
import About from "./components/About";
import Projects from "./components/Projects";
import Footer from "./components/Footer";

const App = () => {
  return (
    <div className="bg-gray-100 min-h-screen">
      <Hero />
      <About />
      <Projects />
      <Footer />
    </div>
  );
};

export default App;
import React from "react";

const Hero = () => {
  return (
    <section className="bg-blue-600 text-white text-center py-20">
      <h1 className="text-5xl font-bold">Welcome to My Portfolio</h1>
      <p className="mt-4 text-xl">Frontend Developer | React Enthusiast</p>
      <button className="mt-8 px-6 py-2 bg-white text-blue-600 rounded hover:bg-gray-200">
        View My Work
      </button>
    </section>
  );
};

export default Hero;
import React from "react";

const About = () => {
  return (
    <section className="py-16 px-8">
      <h2 className="text-3xl font-semibold text-gray-700 mb-4">About Me</h2>
      <p className="text-gray-600">
        I am a passionate developer specializing in building responsive web applications using modern technologies like React and TailwindCSS.
      </p>
    </section>
  );
};

export default About;
import React from "react";

const projects = [
  { title: "Project 1", description: "A cool project with React." },
  { title: "Project 2", description: "Another amazing project." },
];

const Projects = () => {
  return (
    <section className="py-16 px-8 bg-gray-50">
      <h2 className="text-3xl font-semibold text-gray-700 mb-6">Projects</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {projects.map((project, index) => (
          <div key={index} className="p-4 bg-white shadow rounded">
            <h3 className="text-xl font-bold">{project.title}</h3>
            <p className="mt-2 text-gray-600">{project.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Projects;
import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white text-center py-4">
      <p>© 2025 My Portfolio. All rights reserved.</p>
    </footer>
  );
};

export default Footer;module.exports = {
  content: ["./src/*/.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
