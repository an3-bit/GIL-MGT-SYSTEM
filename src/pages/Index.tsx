
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Index = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = () => {
    setIsLoading(true);
    navigate('/login');
  };

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-secondary to-primary">
      <div className="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl w-full">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-8 animate-fadeIn">
              <div className="space-y-4">
                <h1 className="text-4xl md:text-6xl font-bold text-white">
                  Delivering clear, reliable{' '}
                  <span className="text-red-400">solutions</span>
                </h1>
                <h2 className="text-xl md:text-2xl text-white/80">
                  for Great Guardian Investment Ltd at accessible rates.
                </h2>
                <p className="text-lg text-white/60">
                  Our proven methods are designed to simplify, accelerate, and support your property needs.
                </p>
              </div>
              
              <div className="flex gap-4">
                <button
                  onClick={handleLogin}
                  disabled={isLoading}
                  className="btn-primary px-8 py-3 text-lg"
                >
                  {isLoading ? 'Please wait...' : 'Login'}
                </button>
                <button
                  onClick={() => navigate('/register')}
                  className="btn-secondary px-8 py-3 text-lg"
                >
                  Register
                </button>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
