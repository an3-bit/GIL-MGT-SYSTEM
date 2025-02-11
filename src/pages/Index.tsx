
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
    <div className="min-h-screen flex flex-col bg-[#1A1F2C]">
      <div className="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl w-full">
          <div className="space-y-16">
            <div className="space-y-8 animate-fadeIn">
              <div className="space-y-6 text-center">
                <h1 className="text-4xl md:text-6xl font-bold text-white max-w-4xl mx-auto leading-tight">
                  Delivering clear, reliable{' '}
                  <span className="text-red-400">solutions</span> for Great
                  Guardian Investment Ltd at accessible rates.
                </h1>
                <p className="text-xl text-gray-400 max-w-2xl mx-auto">
                  Our proven methods are designed to simplify, accelerate, and support your property needs.
                </p>
              </div>
              
              <div className="flex gap-4 justify-center">
                <button
                  onClick={handleLogin}
                  disabled={isLoading}
                  className="bg-[#1EAEDB] hover:bg-[#0FA0CE] text-white font-medium px-12 py-3 rounded-full transition-colors"
                >
                  {isLoading ? 'Please wait...' : 'Login'}
                </button>
                <button
                  onClick={() => navigate('/register')}
                  className="bg-[#1EAEDB] hover:bg-[#0FA0CE] text-white font-medium px-12 py-3 rounded-full transition-colors"
                >
                  Register
                </button>
                <button
                  onClick={() => navigate('/dashboard')}
                  className="border-2 border-[#1EAEDB] text-[#1EAEDB] hover:bg-[#1EAEDB] hover:text-white font-medium px-12 py-3 rounded-full transition-colors"
                >
                  Dashboard
                </button>
              </div>
            </div>

            <div className="flex justify-center">
              <div className="relative w-96 h-96">
                <div className="absolute inset-0 bg-gradient-to-br from-[#1EAEDB]/20 to-[#0FA0CE]/20 rounded-full blur-3xl"></div>
                <img
                  src="/public/lovable-uploads/c1f402d5-3226-4b1d-b12c-1e567e5ce8d2.png"
                  alt="Title Deeds"
                  className="relative rounded-full w-full h-full object-cover shadow-2xl animate-fadeIn"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
