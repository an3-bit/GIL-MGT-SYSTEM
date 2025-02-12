import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from "./pages/Index";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Clients from "./pages/Clients";
import Surveyors from "./pages/Surveyors";
import Payments from "./pages/Payments";
import Messages from "./pages/Messages";
import NotFound from "./pages/NotFound";
import { Sidebar } from "./components/layout/Sidebar";

const queryClient = new QueryClient();

// Dashboard Layout Component
const DashboardLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-grow p-4">
        {children}
      </div>
    </div>
  );
};

const App = () => {
  const isAuthPage = ["/", "/login", "/register"].includes(window.location.pathname);

  return (
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />

            {/* Dashboard Layout Routes */}
            <Route
              path="/dashboard"
              element={
                <DashboardLayout>
                  <Dashboard />
                </DashboardLayout>
              }
            />
            <Route
              path="/clients"
              element={
                <DashboardLayout>
                  <Clients />
                </DashboardLayout>
              }
            />
            <Route
              path="/surveyors"
              element={
                <DashboardLayout>
                  <Surveyors />
                </DashboardLayout>
              }
            />
            <Route
              path="/payments"
              element={
                <DashboardLayout>
                  <Payments />
                </DashboardLayout>
              }
            />
            <Route
              path="/messages"
              element={
                <DashboardLayout>
                  <Messages />
                </DashboardLayout>
              }
            />

            <Route path="*" element={<NotFound />} />
          </Routes>
        </BrowserRouter>
      </TooltipProvider>
    </QueryClientProvider>
  );
};

export default App;
