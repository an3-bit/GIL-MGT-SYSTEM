
import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Users, CreditCard, MessageSquare, Settings, Menu, X } from 'lucide-react';

export const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(true);
  const location = useLocation();

  const navItems = [
    { icon: LayoutDashboard, label: 'Dashboard', path: '/dashboard' },
    { icon: Users, label: 'Surveyors', path: '/surveyors' },
    { icon: Users, label: 'Clients', path: '/clients' },
    { icon: CreditCard, label: 'Payments', path: '/payments' },
    { icon: MessageSquare, label: 'Messages', path: '/messages' },
    { icon: Settings, label: 'Settings', path: '/settings' },
  ];

  return (
    <>
      <button
        className="lg:hidden fixed top-4 left-4 z-50 p-2 bg-white rounded-md shadow-md"
        onClick={() => setIsOpen(!isOpen)}
      >
        {isOpen ? <X size={20} /> : <Menu size={20} />}
      </button>

      <aside className={`fixed top-0 left-0 z-40 h-screen transition-all duration-300 
        ${isOpen ? 'w-64' : 'w-0 lg:w-64'} overflow-hidden bg-[#1a2234]`}>
        <div className="flex h-full flex-col">
          <div className="flex items-center gap-2 px-6 py-4">
            <img src="/lovable-uploads/7bd0b0d0-63a2-4090-b64a-6e5e9e61b8d9.png" alt="Logo" className="h-8 w-8" />
            <span className="text-lg font-semibold text-white">Easy Manage</span>
          </div>

          <div className="px-4 py-2">
            <span className="text-xs font-semibold text-gray-400 uppercase">MAIN</span>
          </div>

          <nav className="flex-1 space-y-1 px-2 py-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md transition-colors duration-200
                    ${isActive 
                      ? 'bg-blue-600 text-white' 
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
                >
                  <Icon size={20} />
                  <span>{item.label}</span>
                </Link>
              );
            })}
          </nav>
        </div>
      </aside>

      <div className={`lg:pl-64 transition-all duration-300 ${isOpen ? 'pl-64' : 'pl-0'}`}>
        <main className="min-h-screen bg-gray-100">
          {/* Main content will be rendered here */}
        </main>
      </div>
    </>
  );
};
