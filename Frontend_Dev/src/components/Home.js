import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Home.css'; // Optional if you want to add custom styles
import { AuthContext } from './AuthContext';

const Home = () => {
  const { user } = useContext(AuthContext); // Get user from AuthContext
  const navigate = useNavigate(); // Hook to navigate programmatically

  const handleStartQuiz = () => {
    if (user) {
      navigate('/quiz'); // Navigate to the quiz page if user is signed in
    } else {
      alert('You need to sign in to start the quiz'); // Alert if user is not signed in
    }
  };

  return (
    <div className="container my-5">
      <div className="hero-section text-center mb-5">
        <h1 className="display-4">Welcome to QuizApp!</h1>
        <p className="lead">Challenge your mind, sharpen your knowledge, and have fun while learning!</p>
      </div>

      <section className="history-section mb-5">
        <h2 className="mb-3">The History of Quizzes</h2>
        <p>
          Quizzes have been around for centuries as a fun and engaging way to test knowledge. The word "quiz" is thought to have originated in the late 18th century, although its exact origin is debated. Initially, quizzes were informal and often used in social settings as brain-teasers or puzzles to challenge friends.
        </p>
        <p>
          In the 20th century, quizzes became more formalized and were adopted by educational institutions as a means of assessing students' understanding of various subjects. Today, quizzes are not only used in classrooms but also on television shows, social media, and interactive websites, becoming a global phenomenon.
        </p>
      </section>

      <section className="importance-section mb-5">
        <h2 className="mb-3">Why Are Quizzes Important?</h2>
        <p>
          Quizzes are more than just a way to test what you know—they help reinforce your learning. When you take a quiz, you engage in active recall, a proven technique for boosting memory retention. By retrieving information, you solidify the knowledge in your brain, making it easier to recall in the future.
        </p>
        <p>
          Additionally, quizzes offer immediate feedback. This allows you to identify gaps in your knowledge, so you can focus on areas that need improvement. This form of self-assessment is key to mastering any subject, whether it's history, science, mathematics, or general knowledge.
        </p>
      </section>

      <section className="mental-benefits-section mb-5">
        <h2 className="mb-3">What Quizzes Do to Your Brain</h2>
        <p>
          Quizzes stimulate your brain in numerous ways:
        </p>
        <ul>
          <li><strong>Boosts Memory:</strong> Regular quizzing improves your ability to recall information and strengthens neural pathways.</li>
          <li><strong>Encourages Critical Thinking:</strong> Many quiz questions require you to analyze and synthesize information, promoting deeper understanding.</li>
          <li><strong>Increases Focus:</strong> Concentrating on finding the correct answers helps enhance your attention to detail.</li>
          <li><strong>Reduces Cognitive Decline:</strong> Engaging in regular mental challenges like quizzes can help keep your brain sharp, reducing the risk of age-related memory loss.</li>
        </ul>
        <p>
          By frequently taking quizzes, you train your brain to retain information better, which is useful not just for school, but for life in general.
        </p>
      </section>

      <section className="academic-benefits-section mb-5">
        <h2 className="mb-3">How Quizzes Improve Your Grades</h2>
        <p>
          Regularly taking quizzes can have a direct positive impact on your academic performance. Here's how:
        </p>
        <ul>
          <li><strong>Reinforces Learning:</strong> By testing yourself regularly, you're continually reinforcing the material, which helps during exams and class assessments.</li>
          <li><strong>Time Management:</strong> Timed quizzes teach you to work under pressure and manage your time effectively during tests.</li>
          <li><strong>Identifies Weaknesses:</strong> Quizzes highlight the areas where you're struggling, allowing you to focus your study efforts efficiently.</li>
        </ul>
        <p>
          Many students find that incorporating quizzes into their study routine significantly boosts their grades. It’s a fun way to prepare for exams and a break from traditional study methods.
        </p>
      </section>

      <section className="growth-mindset-section mb-5">
        <h2 className="mb-3">Developing a Growth Mindset with Quizzes</h2>
        <p>
          Taking quizzes also fosters a growth mindset, a concept coined by psychologist Carol Dweck. A growth mindset is the belief that abilities and intelligence can be developed through dedication and hard work. Quizzes help cultivate this mindset by encouraging perseverance and resilience.
        </p>
        <p>
          Here’s how quizzes can help you develop grit and a growth mindset:
        </p>
        <ul>
          <li><strong>Embrace Challenges:</strong> Each quiz presents a new challenge, and by taking on these challenges, you learn to see failure as an opportunity for growth.</li>
          <li><strong>Persistence:</strong> The more quizzes you take, the more you strengthen your ability to keep going, even when things get tough.</li>
          <li><strong>Effort Over Time:</strong> Consistent effort over time, including practicing through quizzes, leads to improvement and success.</li>
        </ul>
        <p>
          When you approach learning with a growth mindset, you'll be more motivated to learn, and you’ll find that your grades, as well as your overall mindset, improve.
        </p>
      </section>

      <div className="text-center mb-5">
        <h3>Start Quizzing Now!</h3>
        <p>
          Ready to boost your brainpower, improve your grades, and develop a growth mindset? Start exploring our quizzes today and see how much fun learning can be!
        </p>
        <button className="btn btn-primary" onClick={handleStartQuiz}>Take a Quiz</button>
      </div>
    </div>
  );
};

export default Home;