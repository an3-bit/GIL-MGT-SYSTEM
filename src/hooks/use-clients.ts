
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '@/lib/api-client';
import { toast } from '@/components/ui/use-toast';

interface Client {
  id: number;
  name: string;
  email: string;
  phone: string;
}

export function useClients() {
  const queryClient = useQueryClient();

  const { data: clients, isLoading, error } = useQuery({
    queryKey: ['clients'],
    queryFn: () => apiClient.get('/v1/clients/'),
  });

  const createMutation = useMutation({
    mutationFn: (newClient: Omit<Client, 'id'>) => 
      apiClient.post('/v1/clients/', newClient),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['clients'] });
      toast({
        title: "Success",
        description: "Client created successfully",
      });
    },
    onError: (error) => {
      toast({
        title: "Error",
        description: "Failed to create client",
        variant: "destructive",
      });
      console.error('Create client error:', error);
    },
  });

  const updateMutation = useMutation({
    mutationFn: ({ id, ...data }: Client) => 
      apiClient.put(`/v1/clients/${id}/`, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['clients'] });
      toast({
        title: "Success",
        description: "Client updated successfully",
      });
    },
    onError: (error) => {
      toast({
        title: "Error",
        description: "Failed to update client",
        variant: "destructive",
      });
      console.error('Update client error:', error);
    },
  });

  const deleteMutation = useMutation({
    mutationFn: (id: number) => 
      apiClient.delete(`/v1/clients/${id}/`),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['clients'] });
      toast({
        title: "Success",
        description: "Client deleted successfully",
      });
    },
    onError: (error) => {
      toast({
        title: "Error",
        description: "Failed to delete client",
        variant: "destructive",
      });
      console.error('Delete client error:', error);
    },
  });

  return {
    clients,
    isLoading,
    error,
    createClient: createMutation.mutate,
    updateClient: updateMutation.mutate,
    deleteClient: deleteMutation.mutate,
  };
}
